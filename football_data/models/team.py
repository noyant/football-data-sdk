from pydantic import BaseModel
from typing import Optional, List
from .area import Area
from .season import Season
from .competition import Competition
from .coach import Coach
from .player import Player

class Team(BaseModel):
    id: int
    name: str
    shortName: Optional[str]
    tla: Optional[str]
    crest: Optional[str]
    address: Optional[str]
    website: Optional[str]
    founded: Optional[int]
    clubColors: Optional[str]
    venue: Optional[str]
    area: Optional[Area]
    runningCompetitions: List[Competition] = []
    coach: Optional[Coach] = None
    squad: List[Player] = []

class TeamsResponse(BaseModel):
    count: int
    filters: dict
    season: Season
    teams: List[Team]

class CompetitionTeamResponse(BaseModel):
    count: int
    filters: dict
    season: Season
    teams: List[Team]

class AllTeamsResponse(BaseModel):
    count: int
    filters: dict
    teams: List[Team]
