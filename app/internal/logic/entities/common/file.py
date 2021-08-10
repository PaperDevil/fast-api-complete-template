from typing import Optional

from pydantic import BaseModel


class File(BaseModel):
    full_url: Optional[str]
    short_url: Optional[str]
    prefix_name: Optional[str]
    optional_url: Optional[str]
