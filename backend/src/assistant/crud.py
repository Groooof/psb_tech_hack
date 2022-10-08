import asyncpg
import typing as tp


async def get_passport_validity(con: asyncpg.Connection, passport_series: str, passport_number: str) -> tp.Optional[str]:
    query = '''
    SELECT validity FROM fms WHERE passport_series=$1 AND passport_number=$2;
    '''
    res = await con.fetchval(query, passport_series, passport_number)
    return res


async def get_user_profit(con: asyncpg.Connection, surname, name, patronymic, birthday, document_type, passport_series, passport_number) -> tp.Optional[int]:
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
    query = '''
    SELECT monthly_load, overdue FROM bki WHERE 
    passport_series = $1 AND 
    passport_number = $2;
    '''
    res = await con.fetchrow(query, passport_series, passport_number)
    return (res['monthly_load'], res['overdue']) if res is not None else None


async def test_select(con: asyncpg.Connection):
    query = '''
    SELECT * FROM users;
    '''
    res = await con.fetch(query)
    return res
