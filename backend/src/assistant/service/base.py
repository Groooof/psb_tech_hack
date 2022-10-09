import fastapi
from fastapi import status
from src.assistant import schemas as sch
from src.assistant import crud
from src.assistant.service.external_api import api as ext_api
from src.assistant import utils
import asyncpg
import typing as tp


async def _check_passport(con: asyncpg.Connection, passport_series, passport_number) -> fastapi.Response:
    """
    Проверяем срок действия паспорта при помощи эмулированного API к внешним сервисам (ФМС).
    Если просрочен - кидаем 400 ошибку.
    :param con: асинхронное подключение к бд;
    :param passport_series: серия паспорта;
    :param passport_number: номер паспорта;
    :return: действителен.
    """
    is_valid_passport = await ext_api.FmsApi.is_valid_passport(con, passport_series, passport_number)
    if not is_valid_passport:
        return status.HTTP_400_BAD_REQUEST


async def _check_profit(con, user_data: sch.RequestUserData) -> tp.Union[int, fastapi.Response]:
    """
    Получаем доход клиента за последние 6 месяцев при помощи эмулированного API к внешним сервисам.
    Если доход нулевой, либо не найден - кидаем 400 ошибку;
    :param con: асинхрнное подключение к бд;
    :param user_data: данные пользователя;
    :return: доход.
    """
    fns_profit = await ext_api.FnsApi.get_client_profit(con, user_data.surname, user_data.name, user_data.patronymic,
                                                        user_data.birthday, user_data.document_type,
                                                        user_data.passport_series, user_data.passport_number)
    if fns_profit == 0:
        return status.HTTP_400_BAD_REQUEST
    return fns_profit


async def _get_monthly_load_and_check_overdue(con, passport_series, passport_number) -> tp.Union[int, fastapi.Response]:
    """
    Получаем ежемесячную нагрузку (сумма всех кредитных обязательств) и проверяем на наличие задолженностей.
    Если есть задолженности - кидаем 400 ошибку.
    :param con: асинхронное соединение с бд;
    :param passport_series: серия паспорта;
    :param passport_number: номер паспорта;
    :return: ежемесячная нагрузка.
    """
    monthly_load, overdue = await ext_api.BkiApi.get_monthly_load_and_overdue(con, passport_series, passport_number)
    if overdue:
        return status.HTTP_400_BAD_REQUEST
    return monthly_load


class AvailableCreditProductsCollector:
    """
    Вспомогательный класс для удобного сбора подходящих пользователю кредитных продуктов.
    """
    def __init__(self, con: asyncpg.Connection):
        """
        Принимаем асинхронное подключение к бд для имитации обращения к внешним сервисам и базе данных банка.
        :param con:
        """
        self.con = con
        # специальная структура для хранения подобранных кредитных продуктов
        self.storage = sch.ResponseAvailableCreditProducts()

    async def _get_credit_cards(self, benefits, amount) -> tp.List[dict]:
        """
        Получение кредитных карточек по заданным условиям.
        :param benefits: наличие льгот;
        :param amount: запрашиваемая сумма кредита;
        :return: список подобранных кредитных карт.
        """
        return await crud.get_credit_cards(self.con, benefits, amount)

    async def _get_mortgages(self, benefits, amount, purpose) -> tp.Optional[tp.List[dict]]:
        """
        Получение ипотечных кредитов по заданным условиям.
        :param benefits: наличие льгот;
        :param amount: запрашиваемая сумма кредита;
        :param purpose: цель получения кредита;
        :return: список подобранных ипотечных кредитов либо None.
        """
        # если в качестве цели указана "квартира" - производим поиск по ипотекам
        if purpose == sch.CreditPurposes.flat:
            return await crud.get_mortgages(self.con, benefits, amount)

    async def _get_consumer_credits(self, benefits, amount) -> tp.List[dict]:
        """
        Получение потребительских кредитов по заданным условиям.
        :param benefits: наличие льгот;
        :param amount: запрашиваемая сумма кредита;
        :return: None.
        """
        return await crud.get_consumer_credits(self.con, benefits, amount)

    async def collect_credit_cards(self, benefits, amount) -> None:
        """
        Получаем из бд список подходящих кредитных карт и записываем в хранилище.
        :param benefits: наличие льгот;
        :param amount: запрашиваемая сумма кредита;
        :return: None.
        """
        credit_cards = await self._get_credit_cards(benefits, amount)
        for credit_card in credit_cards:
            available_credit_info = sch.AvailableCreditInfo(name=credit_card['name'])
            self.storage.min_overpayment.append(available_credit_info)
            self.storage.min_monthly_payment.append(available_credit_info)

    async def collect_consumer_credits_and_mortgages(self, benefits: bool, amount: int, purpose: str, available_funds: float) -> None:
        """
        Получаем из бд список потребительских и ипотечных условий, исходя из полученных данных о пользователе.
        :param benefits: наличие льгот;
        :param amount: запрашиваемая сумма кредита;
        :param purpose: цель оформления кредита;
        :param available_funds: рассчитанные "свободные" средства пользователя;
        :return: None.
        """
        # собираем все подходящие потребительские кредитные продукты
        credits_and_mortgages = await self._get_consumer_credits(benefits, amount)
        # собираем также ипотечные продукты, если указана цель "квартира" (flat)
        mortgages = await self._get_mortgages(benefits, amount, purpose)
        if mortgages is not None:
            credits_and_mortgages += mortgages

        for credit_product in credits_and_mortgages:
            # Далее, для каждого продукта ...
            name = credit_product['name']
            interest_rate = credit_product['min_interest_rate']
            max_period = credit_product['max_period']
            min_period = credit_product['min_period']

            # рассчитываем ежемесячный платеж (минимальный) для максимального срока кредита
            monthly_payment_for_max_period = utils.get_credit_monthly_payment(amount,
                                                                              interest_rate,
                                                                              max_period)

            # если полученный платеж больше свободных средств клиента - пропускаем
            if monthly_payment_for_max_period > available_funds:
                continue

            # далее, рассчитываем переплату для максимального срока
            overpayment_for_max_period = utils.get_credit_overpayment(max_period,
                                                                      monthly_payment_for_max_period,
                                                                      amount)
            # создаем dto и записываем в него полученные данные
            available_credit_info = sch.AvailableCreditInfo(name=name,
                                                            monthly_payment=monthly_payment_for_max_period,
                                                            period=max_period,
                                                            overpayment=overpayment_for_max_period,
                                                            interest_rate=interest_rate)
            # записываем в хранилище
            self.storage.min_monthly_payment.append(available_credit_info)

            # следующим этапом рассчитываем данные, но уже для получения максимального ежемесячного платежа
            # при минимальном сроке кредита
            # рассчитываем срок
            period_for_max_monthly_payment = utils.get_credit_period(amount, interest_rate, available_funds)

            # если срок получился меньше допустимого минимального данным кредитом - перерасчитываем для минимального
            if period_for_max_monthly_payment < min_period:
                # наибольший возможный ежемесячный платеж
                available_funds = utils.get_credit_monthly_payment(amount, interest_rate, min_period)
                period_for_max_monthly_payment = min_period

            # также, считаем переплату по кредиту
            overpayment_for_max_monthly_payment = utils.get_credit_overpayment(period_for_max_monthly_payment,
                                                                               available_funds,
                                                                               amount)
            # записываем в dto, затем - в хранилище
            available_credit_info = sch.AvailableCreditInfo(name=name,
                                                            monthly_payment=available_funds,
                                                            period=period_for_max_monthly_payment,
                                                            overpayment=overpayment_for_max_monthly_payment,
                                                            interest_rate=interest_rate)
            self.storage.min_overpayment.append(available_credit_info)

    def get_available(self, sort=False) -> sch.ResponseAvailableCreditProducts:
        """
        Получаем собранные данные с возможностью сортировки.
        :param sort: сортировать?
        :return: структура с собранными кредитными продуктами.
        """
        if not sort:
            return self.storage
        self.storage.min_overpayment.sort(key=lambda item: item.overpayment
        if item.overpayment is not None else float('inf'))
        self.storage.min_monthly_payment.sort(key=lambda item: item.monthly_payment
        if item.monthly_payment is not None else float('inf'))
        return self.storage


async def get_available_credits(con: asyncpg.Connection, user_data: sch.RequestUserData) -> sch.ResponseAvailableCreditProducts:
    """
    На основе полученных от пользователя данных, их проверка на валидность (при помощи сымитированных внешних сервисов)
    и подбор доступных и наиболее выгодных для него кредитных продуктов.
    :param con: асинхронное соединение с базой данных;
    :param user_data: входные данные о пользователе;
    :return: специальная структура данных с подходящими кредитными продуктами.
    """
    await _check_passport(con, user_data.passport_series, user_data.passport_number)  # проверка паспорта
    fns_profit = await _check_profit(con, user_data)  # получение уровня дохода
    # получение ежемесячной нагрузки (суммы ежемесячных кредитных обязательств)
    monthly_load = await _get_monthly_load_and_check_overdue(con, user_data.passport_series, user_data.passport_number)
    available_funds = utils.get_available_funds(fns_profit, monthly_load)  # расчет доступной максимальной суммы для займа

    collector = AvailableCreditProductsCollector(con)
    await collector.collect_credit_cards(user_data.benefits, user_data.amount)  # сбор подходящий кредитных карточек
    # сбор подходящих потребительских и ипотечных кредитов
    await collector.collect_consumer_credits_and_mortgages(user_data.benefits, user_data.amount, user_data.purpose, available_funds)
    return collector.get_available(sort=True)  # получение результирующего списка


