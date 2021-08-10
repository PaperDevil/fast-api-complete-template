from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class LogRequest(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    method: Optional[str]
    url: Optional[str]
    status_code: Optional[int]
    process_time: Optional[int]
    ip: Optional[str]
    headers: Optional[str]
    body: Optional[str]
    query_params: Optional[str]
    error_msg: Optional[str]
