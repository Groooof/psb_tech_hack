from src.database import database
from fastapi import Depends
import sqlalchemy.ext.asyncio as as_sa


def get_db_connection(con: as_sa.AsyncConnection = Depends(database.connection)):
    return con
