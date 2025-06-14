from pydantic import BaseModel
from typing import Optional

class ScoreDetail(BaseModel):
    home: Optional[int]
    away: Optional[int]

class Score(BaseModel):
    winner: Optional[str]
    duration: Optional[str]
    fullTime: Optional[ScoreDetail]
    halfTime: Optional[ScoreDetail] 