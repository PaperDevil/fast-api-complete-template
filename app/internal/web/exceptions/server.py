from fastapi import HTTPException


class ServerExceptionsEnum:
    UNKNOWN_SERVER_ERROR = HTTPException(status_code=500, detail='Неизвестная ошибка сервера')
    NOT_IMPLEMENTED_API = HTTPException(status_code=501, detail='Данный функционал находится в разработке')
