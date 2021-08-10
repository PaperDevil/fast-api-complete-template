from typing import Optional

from app.internal.logic.dao.user import UserDao
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.base import BaseService
from app.internal.web.exceptions.user import UserExceptionEnum


class UserService(BaseService):
    @staticmethod
    async def register(user: User) -> User:
        exist_user: Optional[User] = await UserDao().get_by_phone(user.phone)
        if exist_user:
            raise UserExceptionEnum.PHONE_ALREADY_EXIST

        user.generate_random_password()
        user.create_hash_password()

        user: User = await UserDao().add(user)
        user.create_auth_token()
        user.create_refresh_token()

        return user

    @staticmethod
    async def update(user_id: int, user: User) -> Optional[User]:
        user = await UserDao().update(user_id, user)
        return user

    @staticmethod
    async def auth_user_base(user: User) -> User:
        exist_user: Optional[User] = await UserDao().get_by_phone(user.phone)
        if not exist_user or not User.is_password_valid(user.password, exist_user.hash_password):
            raise UserExceptionEnum.WRONG_EMAIL_OR_PASSWORD
        exist_user.create_auth_token()
        exist_user.create_refresh_token()

        return exist_user

    @staticmethod
    async def get_by_id_simple(user_id: int) -> Optional[User]:
        user: Optional[User] = await UserDao().get_by_id(user_id)
        return user
