from asyncpgsa import create_pool
from typing import Optional


from asyncpg.pool import Pool


class AsyncPg:

    __pool_primary_db: Optional[Pool] = None
    __pool_log_db: Optional[Pool] = None

    @classmethod
    def get_pool_primary_db(cls) -> Pool:
        return cls.__pool_primary_db

    @classmethod
    def get_pool_log_db(cls) -> Pool:
        return cls.__pool_log_db

    @classmethod
    async def init_primary_db(cls, host: str, user: str, password: str, port: int, database: str,
                              min_size: Optional[int] = 10, max_size: Optional[int] = 10):
        cls.__pool_primary_db = await create_pool(host=host, user=user, password=password, port=port, database=database,
                                                  min_size=min_size, max_size=max_size)

    @classmethod
    async def init_log_db(cls, host: str, user: str, password: str, port: int, database: str):
        cls.__pool_log_db = await create_pool(host=host, user=user, password=password, port=port, database=database)

    @classmethod
    async def close_primary_pool_db(cls) -> None:
        await cls.__pool_primary_db.close()

    @classmethod
    async def close_logs_pool_db(cls) -> None:
        await cls.__pool_log_db.close()