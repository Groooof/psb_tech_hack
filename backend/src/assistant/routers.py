from fastapi import APIRouter, Depends
from src.assistant.dependencies import get_db_connection
import sqlalchemy.ext.asyncio as as_sa
from src.assistant import crud


router = APIRouter(prefix='/api/v1', tags=['assistant'])


@router.get('/')
async def test(con: as_sa.AsyncConnection = Depends(get_db_connection)):
    res = await crud.test_select(con)
    return {'res': res}
