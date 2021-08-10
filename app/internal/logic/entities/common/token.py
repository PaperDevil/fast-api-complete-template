from pydantic import Field

from app.internal.logic.entities.response.base import AbstractResponseModel


class Token(AbstractResponseModel):
    token: str = Field(..., example='eyJhbGciOiJIUR5cCI6IkpXVCJ9.eyJzdWIiOiIxWxzZSwiZXhwIjojIyNTU1MDc2LC')
    token_type: str = Field(..., example='bearer')
