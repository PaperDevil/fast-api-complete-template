from typing import Optional

from pydantic import Field

from app.internal.logic.entities.db.user import User
from app.internal.logic.entities.request.base import AbstractRequestModel


class UserAddRequest(AbstractRequestModel):
    phone_number: str = Field(..., min_length=10, max_length=12, example='9503184625')
    first_name: str = Field(..., max_length=32, example='Иван')
    middle_name: Optional[str] = Field(None, max_length=32, example='Иванович')
    last_name: str = Field(..., max_length=32, example='Иванов')

    def to_user(self) -> User:
        return User(
            phone=self.phone_number,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name
        )
