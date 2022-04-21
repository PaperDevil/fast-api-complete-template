from asyncpg import Record

from app.internal.logic.deserializers.base import BaseDeserializer
from app.internal.logic.entities.db.user import User
from app.internal.web.depends.auth import MyOAuth2PasswordRequestForm


class UserDeserializer(BaseDeserializer):
    @staticmethod
    def get_from_db(record: Record) -> User:
        return User(
            id=record.get('user_id'),
            created_at=record.get('user_created_at'),
            edited_at=record.get('user_edited_at'),
            is_delete=record.get('user_is_delete'),
            phone=record.get('user_phone'),
            email=record.get('user_email'),
            login=record.get('user_login'),
            hash_password=record.get('user_hash_password'),
            first_name=record.get('user_first_name'),
            middle_name=record.get('user_middle_name'),
            last_name=record.get('user_last_name')
        )

    @staticmethod
    def get_from_form_data(form_data: MyOAuth2PasswordRequestForm) -> User:
        return User(
            phone=form_data.username,
            password=form_data.password
        )
