from src.database import database
from fastapi import Depends
import asyncpg


def get_db_connection(con: asyncpg.Connection = Depends(database.connection)):
    return con
