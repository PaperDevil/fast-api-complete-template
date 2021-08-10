from pydantic import Field

from app.internal.logic.entities.response.base import AbstractResponseModel


class PhotoResponse(AbstractResponseModel):
    shortLink: str = Field(..., example='some-link')
    fullLink: str = Field(..., example='https://some-link')
