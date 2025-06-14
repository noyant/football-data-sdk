from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class Season(BaseModel):
    id: int
    startDate: date
    endDate: date
    currentMatchday: Optional[int]
    winner: Optional[dict] # Winner can be a team, so we might need a Winner model or just use dict for now
    stages: Optional[List[str]] = None 