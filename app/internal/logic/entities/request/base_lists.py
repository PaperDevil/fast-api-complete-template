from typing import Optional

from pydantic import Field

from app.internal.logic.entities.request.base import AbstractRequestModel


class BaseLimitOffsetRequest(AbstractRequestModel):
    limit: Optional[int] = Field(None, emample=100)
    offset: Optional[int] = Field(None, example=0)
