from pydantic import BaseModel
from typing import Optional, List
from .area import Area
from .season import Season

class Competition(BaseModel):
    id: int
    name: str
    code: Optional[str]
    type: Optional[str]
    emblem: Optional[str]
    area: Optional[Area] = None
    currentSeason: Optional[Season] = None
    seasons: List[Season] = []

class CompetitionResponse(BaseModel):
    count: int
    filters: dict
    competitions: List[Competition]
