from fastapi import APIRouter, Depends
from src.assistant.dependencies import get_db_connection
import asyncpg
import src.assistant.schemas as sch
from src.assistant.service.base import get_available_credits


router = APIRouter(prefix='/api/v1', tags=['assistant'])


@router.post('/choose_credits', response_model=sch.ResponseAvailableCreditProducts)
async def test(user_data: sch.RequestUserData, con: asyncpg.Connection = Depends(get_db_connection)):
    # получение всех доступных и подходящих кредитов текущему пользователю
    return await get_available_credits(con, user_data)
