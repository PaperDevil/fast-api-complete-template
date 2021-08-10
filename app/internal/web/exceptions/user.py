from fastapi import HTTPException


class UserExceptionEnum:
    USER_DOESNT_EXISTS = HTTPException(404, detail='Данный аккаунт не существует')
    EMAIL_ALREADY_EXISTS = HTTPException(400, detail='Данный email уже зарегистрирован')
    PHONE_ALREADY_EXIST = HTTPException(400, detail='Данный номер телефона уже зарегистрирован')
    WRONG_EMAIL_OR_PASSWORD = HTTPException(status_code=401, detail='Неверный логин или пароль',
                                            headers={'WWW-Authenticate': 'Bearer'})
    WRONG_AUTH_TOKEN = HTTPException(status_code=401, detail='Некорректный токен',
                                     headers={'WWW-Authenticate': 'Bearer'})
    NO_PERMISSION = HTTPException(403, detail='Недостаточно прав для данного действия')
    INVALID_PHONE_NUMBER = HTTPException(400, detail='Укзан не кореектный номер телефона')
