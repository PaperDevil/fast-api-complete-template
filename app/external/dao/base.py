from asyncpg import Connection
from asyncpg.pool import Pool

from app.internal.drivers.async_pg import AsyncPg


class BaseLogsDao:

    def __init__(self, conn: Connection = None) -> None:
        self.pool: Pool = AsyncPg.get_pool_log_db()
        self.conn: Connection = conn

    async def add(self, obj: object) -> object:
        raise NotImplementedError
