from fastapi import HTTPException


class TokenExceptionEnum:
    EXPIRED = HTTPException(status_code=401, detail='Срок действия токена истёк', headers={'WWW-Authenticate': 'Bearer'})
    INVALID_SCOPE = HTTPException(status_code=401, detail='Неверный тип токена', headers={'WWW-Authenticate': 'Bearer'})
    INVALID = HTTPException(status_code=401, detail='Неверный токен', headers={'WWW-Authenticate': 'Bearer'})
