from typing import Optional, List

from asyncpg import UniqueViolationError
from sqlalchemy import select, func, and_

from app.internal.logic.dao.base import BaseDao
from app.internal.logic.deserializers.user import UserDeserializer
from app.internal.logic.entities.db.user import User
from app.internal.web.exceptions.user import UserExceptionEnum
from app.schema.meta import user_table

EMAIL_UNIQUE_CONSTRAINT = "uq__user__email"
PHONE_UNIQUE_CONSTRAINT = "uq__user__phone"
LOGIN_UNIQUE_CONSTRAINT = "uq__user__login"


class UserDao(BaseDao):
    default_rows = [
        user_table.c.id.label('user_id'),
        user_table.c.created_at.label('user_created_at'),
        user_table.c.edited_at.label('user_updated_at'),
        user_table.c.is_delete.label('user_is_delete'),
        user_table.c.phone.label('user_phone'),
        user_table.c.email.label('user_email'),
        user_table.c.login.label('user_login'),
        user_table.c.hash_password.label('user_hash_password'),
        user_table.c.first_name.label('user_first_name'),
        user_table.c.middle_name.label('user_middle_name'),
        user_table.c.last_name.label('user_last_name')
    ]

    async def add(self, user: User) -> User:
        query = user_table.insert().values(
            phone=user.phone,
            first_name=user.first_name,
            middle_name=user.middle_name,
            last_name=user.last_name,
            hash_password=user.hash_password
        ).returning(user_table.c.id)

        async with self.connection as conn:
            try:
                user_id = await conn.fetchval(query)
            except UniqueViolationError as exc:
                if exc.constraint_name == PHONE_UNIQUE_CONSTRAINT:
                    raise UserExceptionEnum.PHONE_ALREADY_EXIST
                else:
                    raise TypeError

        user.id = user_id
        return user

    async def update(self, id: int, user: User) -> Optional[User]:
        query = user_table.update().values(
            phone=func.coalesce(user.phone, user_table.c.phone),
            email=func.coalesce(user.email, user_table.c.email),
            login=func.coalesce(user.login, user_table.c.login),
            hash_password=func.coalesce(user.hash_password, user_table.c.hash_password),
            first_name=func.coalesce(user.first_name, user_table.c.first_name),
            middle_name=func.coalesce(user.middle_name, user_table.c.middle_name),
            last_name=func.coalesce(user.last_name, user_table.c.last_name)
        ).where(and_(
            user_table.c.id == id,
            user_table.c.is_delete.is_(False)
        )).returning(*self.default_rows)

        async with self.connection as conn:
            try:
                row = await conn.fetchrow(query)
            except UniqueViolationError as exc:
                if exc.constraint_name == PHONE_UNIQUE_CONSTRAINT:
                    raise UserExceptionEnum.PHONE_ALREADY_EXIST
                else:
                    raise TypeError

        if not row:
            return None

        return UserDeserializer.get_from_db(row)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = select(self.default_rows).select_from(user_table).where(
            user_table.c.id == id
        )

        return await self._get_object_by_field(query)

    async def get_by_phone(self, phone: str) -> Optional[User]:
        query = select(self.default_rows).select_from(user_table).where(
            user_table.c.phone == phone
        )

        return await self._get_object_by_field(query)

    async def _get_object_by_field(self, query) -> Optional[User]:
        async with self.connection as conn:
            row = await conn.fetchrow(query)

        if not row:
            return None

        return UserDeserializer.get_from_db(row)
