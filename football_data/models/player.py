from pydantic import BaseModel
from typing import Optional
from datetime import date

class Player(BaseModel):
    id: int
    name: str
    position: Optional[str]
    dateOfBirth: Optional[date]
    nationality: Optional[str] 