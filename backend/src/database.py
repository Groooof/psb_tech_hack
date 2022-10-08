import sqlalchemy.ext.asyncio as as_sa
import sqlalchemy as sa
from sqlalchemy.pool import AsyncAdaptedQueuePool
from abc import ABCMeta, abstractmethod
import typing as tp


def get_postgres_dsn(user: str, password: str, host: str, port: str, db: str,
                     sa_driver: str = None, sa_dialect: str = None):
    dsn_without_prefix = f'{user}:{password}@{host}:{port}/{db}'

    if sa_driver is None and sa_dialect is None:
        base_prefix = 'postgres://'
        return base_prefix + dsn_without_prefix

    sa_prefix = f'{sa_driver}+{sa_dialect}://'
    return sa_prefix + dsn_without_prefix


class IDatabase(metaclass=ABCMeta):

    @abstractmethod
    async def on_startup(self, user: str, password: str, host: str, port: str, db: str) -> None:
        pass

    @abstractmethod
    async def on_shutdown(self) -> None:
        pass

    @abstractmethod
    async def connection(self):
        pass


class AsyncSADatabase(IDatabase):
    driver = 'postgresql'
    dialect = 'asyncpg'

    def __init__(self):
        self.engine: tp.Optional[as_sa.AsyncEngine] = None

    async def on_startup(self, user: str, password: str, host: str, port: str, db: str) -> None:
        dsn = get_postgres_dsn(user, password, host, port, db, self.driver, self.dialect)
        self.engine = as_sa.create_async_engine(dsn, poolclass=AsyncAdaptedQueuePool, pool_size=5, max_overflow=0)

    async def on_shutdown(self) -> None:
        pass

    async def connection(self) -> as_sa.AsyncConnection:
        if self.engine is None:
            raise NotImplementedError('Engine must be created first')
        con = await self.engine.connect()
        try:
            yield con
            await con.commit()
        except Exception as ex:
            con.rollback()
        finally:
            await con.close()


class SyncSADatabase(IDatabase):
    driver = 'postgresql'
    dialect = 'psycopg2'

    def __init__(self):
        self.engine: tp.Optional[sa.engine.Engine] = None

    async def on_startup(self, user: str, password: str, host: str, port: str, db: str) -> None:
        dsn = get_postgres_dsn(user, password, host, port, db, self.driver, self.dialect)
        self.engine = sa.create_engine(dsn)

    async def on_shutdown(self) -> None:
        pass

    async def connection(self) -> as_sa.AsyncConnection:
        if self.engine is None:
            raise NotImplementedError('Engine must be created first')

        con = self.engine.connect()
        try:
            yield con
        except Exception as ex:
            pass
        finally:
            con.close()


database = AsyncSADatabase()
