from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date
from .area import Area
from .competition import Competition
from .season import Season
from .team import Team
from .score import Score

class ResultSet(BaseModel):
    count: int
    competitions: Optional[str] = None
    first: Optional[date] = None
    last: Optional[date] = None
    played: Optional[int] = None
    wins: Optional[int] = None
    draws: Optional[int] = None
    losses: Optional[int] = None

class Match(BaseModel):
    area: Area
    competition: Competition
    season: Season
    id: int
    utcDate: datetime
    status: str
    minute: Optional[str]
    injuryTime: Optional[int]
    attendance: Optional[int]
    venue: Optional[str]
    matchday: Optional[int]
    stage: str
    group: Optional[str]
    lastUpdated: datetime
    homeTeam: Team
    awayTeam: Team
    score: Score
    goals: List = []
    penalties: List = []
    bookings: List = []
    substitutions: List = []
    odds: dict = {}
    referees: List = []

class MatchResponse(BaseModel):
    filters: dict
    resultSet: ResultSet
    matches: List[Match]
