from fastapi import APIRouter, Depends
from src.assistant.dependencies import get_db_connection
import asyncpg
from src.assistant.service.external_api import api as ext_api
from datetime import datetime as dt
import src.assistant.schemas as sch
from fastapi import status
from src.assistant import crud
import math
from src.assistant import utils


router = APIRouter(prefix='/api/v1', tags=['assistant'])


@router.post('/')
async def test(user_data: sch.RequestUserData, con: asyncpg.Connection = Depends(get_db_connection)):
    is_valid_passport = await ext_api.FmsApi.is_valid_passport(con, user_data.passport_series, user_data.passport_number)
    if not is_valid_passport:
        return status.HTTP_400_BAD_REQUEST

    fns_profit = await ext_api.FnsApi.get_client_profit(con, user_data.surname, user_data.name, user_data.patronymic,
                                                       user_data.birthday, user_data.document_type,
                                                       user_data.passport_series, user_data.passport_number)

    if fns_profit == 0:
        return status.HTTP_400_BAD_REQUEST

    monthly_load, overdue = await ext_api.BkiApi.get_monthly_load_and_overdue(con, user_data.passport_series, user_data.passport_number)

    if overdue:
        return status.HTTP_400_BAD_REQUEST

    available_funds = round(((fns_profit / 6) - monthly_load)/2)

    credit_products = await crud.get_consumer_credits(con, user_data.benefits)
    if user_data.purpose == sch.CreditPurposes.flat:
        credit_products += await crud.get_mortgages(con, user_data.benefits)

    available_credit_products = sch.ResponseAvailableCreditProducts()
    for credits_product in credit_products:
        monthly_payment_for_max_period = utils.get_credit_monthly_payment(user_data.amount, credits_product['min_interest_rate'],
                                                           credits_product['max_period'])
        if monthly_payment_for_max_period > available_funds:
            continue

        overpayment_for_max_period = (credits_product['max_period'] * monthly_payment_for_max_period) - user_data.amount
        available_credit_info = sch.AvailableCreditInfo(name=credits_product['name'],
                                                        monthly_payment=monthly_payment_for_max_period,
                                                        period=credits_product['max_period'],
                                                        overpayment=overpayment_for_max_period)
        available_credit_products.min_monthly_payment.append(available_credit_info)

        period_for_max_monthly_payment = utils.get_credit_period(user_data.amount, credits_product['min_interest_rate'],
                                                                 available_funds)
        overpayment_for_max_monthly_payment = (period_for_max_monthly_payment * available_funds) - user_data.amount
        available_credit_info = sch.AvailableCreditInfo(name=credits_product['name'],
                                                        monthly_payment=available_funds,
                                                        period=period_for_max_monthly_payment,
                                                        overpayment=overpayment_for_max_monthly_payment)
        available_credit_products.min_overpayment.append(available_credit_info)

    available_credit_products.min_overpayment.sort(key=lambda item: item.overpayment)
    available_credit_products.min_monthly_payment.sort(key=lambda item: item.monthly_payment)

    return available_credit_products


    # return await ext_api.BkiApi.get_monthly_load_and_overdue(con, '0001', '000001')
    # return await ext_api.FnsApi.get_client_profit(con, 'Бобров', 'Андрей', 'Андреевич', dt(2000, 5, 3), 'паспорт', '0001', '000001')
    # return await ext_api.FmsApi.is_valid_passport(con, '0001', '000001')
