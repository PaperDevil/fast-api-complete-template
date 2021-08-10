from app.external.dao.base import BaseLogsDao
from app.external.entities.log_request import LogRequest


class LogRequestDao(BaseLogsDao):
    async def add(self, log_request: LogRequest) -> None:
        sql = """
            INSERT INTO log_request(method, url, status_code, process_time, ip, headers, body, query_params, error_msg)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
        """

        async with self.pool.acquire() as conn:
            await conn.execute(sql, log_request.method, log_request.url, log_request.status_code, log_request.process_time,
                               log_request.ip, log_request.headers, log_request.body, log_request.query_params, log_request.error_msg)
