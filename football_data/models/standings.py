from pydantic import BaseModel
from typing import Optional, List
from .competition import Competition
from .season import Season
from .team import Team

class TableEntry(BaseModel):
    position: int
    team: Team
    playedGames: int
    form: Optional[str]
    won: int
    draw: int
    lost: int
    points: int
    goalsFor: int
    goalsAgainst: int
    goalDifference: int

class Standing(BaseModel):
    stage: str
    type: str
    group: Optional[str]
    table: List[TableEntry]

class StandingsResponse(BaseModel):
    filters: dict
    competition: Competition
    season: Season
    standings: List[Standing] 