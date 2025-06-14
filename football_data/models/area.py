from pydantic import BaseModel
from typing import Optional, List

class Area(BaseModel):
    id: int
    name: str
    code: str
    flag: Optional[str] = None

class AreasResponse(BaseModel):
    count: int
    filters: dict
    areas: List[Area] 