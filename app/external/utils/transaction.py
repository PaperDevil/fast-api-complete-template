from contextlib import asynccontextmanager

from app.internal.drivers.async_pg import AsyncPg


@asynccontextmanager
async def get_connection_transaction():
    connection = await AsyncPg.get_pool_primary_db().acquire()
    transaction = connection.transaction()
    await transaction.start()
    try:
        yield connection
    except Exception:
        await transaction.rollback()
        raise
    else:
        await transaction.commit()
    finally:
        await AsyncPg.get_pool_primary_db().release(connection)
