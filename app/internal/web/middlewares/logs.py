import time
import traceback

from fastapi import Request, FastAPI
from starlette.responses import JSONResponse

from app.external.dao.log_request import LogRequestDao
from app.external.entities.log_request import LogRequest
from app.internal.web.exceptions.server import ServerExceptionsEnum


def add_logs(app: FastAPI):
    @app.middleware('http')
    async def simple_logs(request: Request, call_next):
        start_time = time.time()
        try:
            response = await call_next(request)
            status_code = response.status_code
            err_msg = None
        except Exception:
            status_code = ServerExceptionsEnum.UNKNOWN_SERVER_ERROR.status_code
            response = JSONResponse(content={'detail': ServerExceptionsEnum.UNKNOWN_SERVER_ERROR.detail}, status_code=status_code)
            err_msg = traceback.format_exc()

        process_time = round((time.time() - start_time) * 1000)
        headers = str(request.headers.items())
        query_params = str(list(request.query_params.items()))
        method = request.method
        ip = request.headers.get('x-real-ip')
        url = str(request.url).split('?')[0]

        await LogRequestDao().add(LogRequest(
            method=method,
            url=url,
            ip=ip,
            headers=headers,
            query_params=query_params,
            body=None,
            status_code=status_code,
            process_time=process_time,
            error_msg=err_msg
        ))

        return response
