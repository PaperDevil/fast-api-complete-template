from typing import Optional

from fastapi import Depends, Security
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

from app.conf.keys import SECRET_KEY, ENCRYPT_ALGORITHM
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.user import UserService
from app.internal.web.exceptions.token import TokenExceptionEnum
from app.internal.web.exceptions.user import UserExceptionEnum

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/auth/base")
security = HTTPBearer()


def get_optional_user_from_token(
    token: str = Depends(oauth2_scheme),
) -> Optional[User]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ENCRYPT_ALGORITHM])
        assert payload['scope'] == 'access_token'
    except AssertionError:
        raise TokenExceptionEnum.INVALID_SCOPE
    except jwt.ExpiredSignatureError:
        raise TokenExceptionEnum.EXPIRED
    except jwt.JWTError:
        raise TokenExceptionEnum.INVALID

    user_id: Optional[str] = payload.get("sub")

    if not user_id:
        return None

    try:
        user_id: int = int(user_id)
    except ValueError:
        return None

    return User(id=user_id)


def get_user_from_refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ENCRYPT_ALGORITHM])
        assert payload['scope'] == 'refresh_token'
    except AssertionError:
        raise TokenExceptionEnum.INVALID_SCOPE
    except jwt.ExpiredSignatureError:
        raise TokenExceptionEnum.EXPIRED
    except jwt.JWTError:
        raise TokenExceptionEnum.INVALID

    user_id: Optional[str] = payload.get("sub")

    if not user_id:
        return None

    try:
        user_id: int = int(user_id)
    except ValueError:
        return None

    return User(id=user_id, refresh_token=refresh_token)


async def get_current_user_from_refresh_token(
    user: User = Depends(get_user_from_refresh_token),
) -> User:
    if not user:
        raise UserExceptionEnum.WRONG_AUTH_TOKEN
    exist_user = await UserService.get_by_id_simple(user.id)
    if not exist_user:
        raise UserExceptionEnum.WRONG_AUTH_TOKEN
    exist_user.refresh_token = user.refresh_token
    return exist_user


async def get_current_user(
    user: User = Depends(get_optional_user_from_token),
) -> User:
    if not user:
        raise UserExceptionEnum.WRONG_AUTH_TOKEN
    account = await UserService.get_by_id_simple(user.id)
    if not account:
        raise UserExceptionEnum.WRONG_AUTH_TOKEN
    return account
