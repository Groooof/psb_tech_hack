from src.database import database
from src.config import env


async def on_startup():
    await database.on_startup(env.POSTGRES_USER, env.POSTGRES_PASSWORD, env.POSTGRES_HOST, env.POSTGRES_PORT, env.POSTGRES_DB)
    print('App is running!')


async def on_shutdown():
    print('App is shutting down!')
