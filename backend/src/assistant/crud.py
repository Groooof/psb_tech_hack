import asyncpg
import typing as tp


async def get_passport_validity(con: asyncpg.Connection, passport_series: str, passport_number: str) -> tp.Optional[str]:
    """
    Обращаемся к таблице, имитирующей сервис ФМС, и получаем срок окончания действия паспорта
    :param con: асинхронное подключение к бд
    :param passport_series: серия паспорта
    :param passport_number: номер паспорта
    :return: срок (дата) окончания действия паспорта
    """
    query = '''
    SELECT validity FROM fms WHERE passport_series=$1 AND passport_number=$2;
    '''
    res = await con.fetchval(query, passport_series, passport_number)
    return res


async def get_user_profit(con: asyncpg.Connection, surname, name, patronymic, birthday, document_type, passport_series, passport_number) -> tp.Optional[int]:
    """
    Обращаемся к таблице, имитирующей сервис ФНС и получаем доход пользователя за последние 6 месяцев
    :param con: асинхронное подключение к бд
    :param surname: фамилия
    :param name: имя
    :param patronymic: отчество
    :param birthday: дата рождения
    :param document_type: тип документа (паспорт)
    :param passport_series: серия паспорта
    :param passport_number: номер паспорта
    :return: доход пользователя за последние 6 месяцев
    """
    query = '''
    SELECT profit FROM fns WHERE 
    surname = $1 AND
    name = $2 AND
    patronymic = $3 AND
    birthday = $4 AND
    document_type = $5 AND
    passport_series = $6 AND
    passport_number = $7;
    '''
    res = await con.fetchval(query, surname, name, patronymic, birthday, document_type, passport_series, passport_number)
    return res


async def get_monthly_load_and_overdue(con: asyncpg.Connection, passport_series: str, passport_number: str) -> tp.Optional[tp.Tuple[int, bool]]:
    """
    Обращаемся к таблице, имитирующей сервис БКИ и получаем ежемесячную кредитную нагрузку пользователя (сумму всех
    ежемесячных кредитных обязательств, которые он на данный момент выплачивает) и наличие задолженностей.
    :param con: асинхронное подключение к бд;
    :param passport_series: серия паспорта;
    :param passport_number: номер паспорта;
    :return: ежемесячная нагрузка и наличие задолженностей
    """
    query = '''
    SELECT monthly_load, overdue FROM bki WHERE 
    passport_series = $1 AND 
    passport_number = $2;
    '''
    res = await con.fetchrow(query, passport_series, passport_number)
    return (res['monthly_load'], res['overdue']) if res is not None else None


async def get_mortgages(con: asyncpg.Connection, benefits: bool, amount: int) -> tp.List[tp.Optional[dict]]:
    """
    Получаем список всех ипотечных кредитов по условиям наличия/отсутствия льгот и запрашиваемой сумме кредита.
    :param con: асинхронное подключение к бд;
    :param benefits: наличие льгот;
    :param amount: сумма кредита;
    :return: список доступных кредитов.
    """
    query = '''
    SELECT * FROM mortgages WHERE 
    benefits = $1 AND
    min_amount <= $2 AND
    max_amount >= $2;
    '''
    res = await con.fetch(query, benefits, amount)
    return res


async def get_consumer_credits(con: asyncpg.Connection, benefits: bool, amount: int) -> tp.List[tp.Optional[dict]]:
    """
    Получаем список всех потребительских кредитов по условиям наличия/отсутствия льгот и запрашиваемой сумме кредита.
    :param con: асинхронное подключение к бд;
    :param benefits: наличие льгот;
    :param amount: сумма кредита;
    :return: список доступных кредитов.
    """
    query = '''
    SELECT * FROM consumer_credits WHERE 
    benefits = $1 AND
    min_amount <= $2 AND
    max_amount >= $2;
    '''
    res = await con.fetch(query, benefits, amount)
    return res


async def get_credit_cards(con: asyncpg.Connection, benefits: bool, amount: int) -> tp.List[tp.Optional[dict]]:
    """
    Получаем список всех кредитных карточек по условиям наличия/отсутствия льгот и запрашиваемой сумме кредита.
    :param con: асинхронное подключение к бд;
    :param benefits: наличие льгот;
    :param amount: сумма кредита;
    :return: список доступных кредитных карточек.
    """
    query = '''
    SELECT * FROM credit_cards WHERE 
    benefits = $1 AND
    min_amount <= $2 AND
    max_amount >= $2;
    '''
    res = await con.fetch(query, benefits, amount)
    return res
