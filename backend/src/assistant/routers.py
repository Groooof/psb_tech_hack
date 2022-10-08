from fastapi import APIRouter, Depends
from src.assistant.dependencies import get_db_connection
import asyncpg
from src.assistant.service.external_api import api as ext_api
from datetime import datetime as dt


router = APIRouter(prefix='/api/v1', tags=['assistant'])


@router.get('/')
async def test(con: asyncpg.Connection = Depends(get_db_connection)):
    return await ext_api.BkiApi.get_monthly_load_and_overdue(con, '0001', '000001')
    # return await ext_api.FnsApi.get_client_profit(con, 'Бобров', 'Андрей', 'Андреевич', dt(2000, 5, 3), 'паспорт', '0001', '000001')
    # return await ext_api.FmsApi.is_valid_passport(con, '0001', '000001')
