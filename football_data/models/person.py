from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from .team import Team

class Person(BaseModel):
    id: int
    name: str
    firstName: Optional[str]
    lastName: Optional[str]
    dateOfBirth: Optional[date]
    nationality: Optional[str]
    section: Optional[str]
    position: Optional[str]
    shirtNumber: Optional[int]
    lastUpdated: Optional[date]
    currentTeam: Optional[Team] 