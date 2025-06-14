__version__ = "0.2.0"

from .client import APIClient
from .endpoints.areas import Areas
from .endpoints.competitions import Competitions
from .endpoints.matches import Matches
from .endpoints.teams import Teams
from .endpoints.standings import Standings
from .endpoints.persons import Persons
from typing import Optional

class FootballData:
    def __init__(self, api_key: Optional[str] = None):
        self.client = APIClient(api_key)
        self.areas = Areas(self.client)
        self.competitions = Competitions(self.client)
        self.matches = Matches(self.client)
        self.teams = Teams(self.client)
        self.standings = Standings(self.client)
        self.persons = Persons(self.client)
