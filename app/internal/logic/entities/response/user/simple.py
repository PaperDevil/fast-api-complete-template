from typing import Optional

from pydantic import Field

from app.internal.logic.entities.response.base import AbstractResponseModel


class UserSimpleResponse(AbstractResponseModel):
    id: Optional[int] = Field(None, example=1)
    phone: Optional[str] = Field(None, example='8-944-123-45-67')
    email: Optional[str] = Field(None, example='test@test.com')
    login: Optional[str] = Field(None, example='nickname')
    name: Optional[str] = Field(None, example='Иван')
