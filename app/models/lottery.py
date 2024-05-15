from pydantic import BaseModel, Field
from typing import Optional

class Lottery(BaseModel):
    name: str
    number: Optional[int] = Field(None)
    completed: Optional[bool] = Field(None)
    winner: Optional[str] = Field(None)
    create_datetime: Optional[str] = Field(None)