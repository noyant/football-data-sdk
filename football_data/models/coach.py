from pydantic import BaseModel
from typing import Optional
from datetime import date

class Coach(BaseModel):
    id: Optional[int]
    firstName: Optional[str]
    lastName: Optional[str]
    name: Optional[str]
    dateOfBirth: Optional[date]
    nationality: Optional[str]
    contract: Optional[dict] 