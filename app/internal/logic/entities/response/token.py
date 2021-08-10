from pydantic import Field

from app.internal.logic.entities.common.token import Token
from app.internal.logic.entities.response.base import AbstractResponseModel


class OldTokensResponse(AbstractResponseModel):
    access_token: Token
    refresh_token: Token


class TokensResponse(AbstractResponseModel):
    access_token: str = Field(..., example='eyJhbGciOiJIUR5cCI6IkpXVCJ9.eyJzdWIiOiIxWxzZSwiZXhwIjojIyNTU1MDc2LC')
    refresh_token: str = Field(..., example='eyJhbGciOiJIUR5cCI6IkpXVCJ9.eyJzdWIiOiIxWxzZSwiZXhwIjojIyNTU1MDc2LC')
