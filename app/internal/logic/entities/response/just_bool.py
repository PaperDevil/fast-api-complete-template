from pydantic import Field

from app.internal.logic.entities.response.base import AbstractResponseModel


class JustBoolResponse(AbstractResponseModel):
    result: bool = Field(..., example=True)
