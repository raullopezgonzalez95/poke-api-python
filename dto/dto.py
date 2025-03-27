from pydantic import BaseModel
from typing import List, Optional


class Result(BaseModel):
    name: str
    url: str


class ResponseData(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Result]
