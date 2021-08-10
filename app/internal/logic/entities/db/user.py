import random
import string
from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from loguru import logger

from app.conf.keys import SECRET_KEY, ENCRYPT_ALGORITHM
from app.external.utils.phone import get_phone_national_number
from app.internal.drivers.cache_driver import CacheDriver
from app.internal.drivers.crypt_driver import CryptDriver
from app.internal.logic.entities.db.base import AbstractDbModel
from app.internal.logic.entities.db.role import Role
from app.internal.logic.entities.response.token import TokensResponse
from app.internal.logic.entities.response.user.detail import UserDetailResponse
from app.internal.logic.entities.response.user.simple import UserSimpleResponse


class User(AbstractDbModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 is_delete: Optional[bool] = None,
                 phone: Optional[str] = None,
                 email: Optional[str] = None,
                 login: Optional[str] = None,
                 password: Optional[str] = None,
                 hash_password: Optional[str] = None,
                 first_name: Optional[str] = None,
                 middle_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 position: Optional[str] = None,
                 role: Optional[Role] = None,
                 head_user: Optional = None,
                 # # # AUTH # # #
                 auth_token: Optional[str] = None,
                 refresh_token: Optional[str] = None,
                 client_data: Optional[dict] = None
                 ):
        super().__init__(id, created_at, edited_at, is_delete)
        self.phone = get_phone_national_number(phone)
        self.email = email
        self.login = login
        self.password = password
        self.hash_password = hash_password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.position = position
        self.role = role
        self.head_user = head_user
        self.auth_token = auth_token
        self.refresh_token = refresh_token
        self.client_data = client_data

    def __repr__(self):
        return f"""
        User(id={self.id}, created_at={self.created_at}, edited_at={self.edited_at}, is_delete={self.is_delete},
        phone={self.phone}, email={self.email}, login={self.login}, password={self.password},
        hash_password={self.hash_password}, first_name={self.first_name}, middle_name={self.middle_name},
        last_name={self.last_name}, position={self.position}, role={self.role}, head_user={self.head_user})
        """

    @staticmethod
    def is_password_valid(password: str, hash_password: str) -> bool:
        return CryptDriver.context.verify(password, hash_password)

    def generate_random_password(self, length=12):
        if self.password:
            return None
        self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def create_hash_password(self) -> None:
        if not self.password:
            return
        self.hash_password = CryptDriver.context.hash(self.password)

    def create_auth_token(self) -> None:
        if not self.id:
            raise TypeError

        self.auth_token = jwt.encode({
            'sub': str(self.id),
            'exp': datetime.now() + timedelta(days=1),
            'iat': datetime.now(),
            'scope': 'access_token',
        }, SECRET_KEY, algorithm=ENCRYPT_ALGORITHM)

    def create_refresh_token(self) -> None:
        if not self.id:
            raise TypeError

        self.refresh_token = jwt.encode({
            'sub': str(self.id),
            'exp': datetime.now() + timedelta(weeks=4),
            'iat': datetime.now(),
            'scope': 'refresh_token',
        }, SECRET_KEY, algorithm=ENCRYPT_ALGORITHM)

    def to_tokens(self) -> TokensResponse:
        return TokensResponse(
            access_token=self.auth_token,
            refresh_token=self.refresh_token
        )

    def create_fast_auth_token(self) -> str:
        if not self.id:
            raise TypeError

        token = jwt.encode({
            'sub': str(self.id),
            'exp': datetime.now() + timedelta(days=1),
            'iat': datetime.now(),
            'scope': 'fast_auth_token',
        }, SECRET_KEY, algorithm=ENCRYPT_ALGORITHM)

        logger.warning(f"user_id: {self.id}, user_token: {token}")
        CacheDriver.set_or_update(self.id, {'fast_auth_token': token})
        return token

    def to_user_detail_response(self) -> UserDetailResponse:
        return UserDetailResponse(
            id=self.id,
            phone=self.phone,
            email=self.email,
            login=self.login,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            fullname=f'{self.last_name} {self.first_name} {self.middle_name}'.strip(),
        )

    def to_user_simple_response(self) -> UserSimpleResponse:
        return UserSimpleResponse(
            id=self.id,
            phone=self.phone,
            email=self.email,
            login=self.login,
            name=self.first_name,
        )
