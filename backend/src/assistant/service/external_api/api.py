import typing as tp
from src.assistant import crud
import asyncpg


class FmsApi:
    """
    Эмуляция API сервиса ФМС (берем данные из бд).
    """
    @staticmethod
    async def is_valid_passport(con: asyncpg.Connection, passport_series, passport_number) -> bool:
        validity = await crud.get_passport_validity(con, passport_series, passport_number)
        return True if validity is not None else False


class FnsApi:
    """
    Эмуляция API сервиса ФНС (берем данные из бд).
    """
    @staticmethod
    async def get_client_profit(con: asyncpg.Connection, surname, name, patronymic, birthday, document_type, passport_series, passport_number) -> int:
        # for last 6 month
        profit = await crud.get_user_profit(con, surname, name, patronymic, birthday, document_type, passport_series, passport_number)
        return profit if profit is not None else 0


class BkiApi:
    """
    Эмуляция API сервиса БКИ (берем данные из бд).
    """
    @staticmethod
    async def get_monthly_load_and_overdue(con: asyncpg.Connection, passport_series, passport_number) -> tp.Optional[tp.Tuple[int, bool]]:
        res = await crud.get_monthly_load_and_overdue(con, passport_series, passport_number)
        return res

