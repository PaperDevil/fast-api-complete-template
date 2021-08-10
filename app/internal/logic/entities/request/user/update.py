from typing import Optional

from pydantic import Field

from app.internal.logic.entities.db.user import User
from app.internal.logic.entities.request.base import AbstractRequestModel


class UserUpdateRequest(AbstractRequestModel):
    email: Optional[str] = Field(None, max_length=100, example='my@mail.ru')
    login: Optional[str] = Field(None, max_length=64, example='Some username')
    first_name: Optional[str] = Field(None, max_length=32, example='Иван')
    middle_name: Optional[str] = Field(None, max_length=32, example='Иванович')
    last_name: Optional[str] = Field(None, max_length=32, example='Иванов')

    def to_user(self) -> User:
        return User(
            email=self.email,
            login=self.login,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name
        )


class UserUpdatePhoneRequest(AbstractRequestModel):
    phone_number: Optional[str] = Field(..., example='9503184625')
    sms_code: Optional[str] = Field(..., max_length=6, example='123456')
