from typing import List, Optional
from football_data.client import APIClient
from football_data.models.standings import Standing, StandingsResponse

class Standings:
    def __init__(self, client: APIClient):
        self.client = client

    def get_for_competition(self, competition_id: int, season: Optional[int] = None) -> List[Standing]:
        """
        Get standings for a given competition.
        :param competition_id: The ID of the competition.
        :param season: The starting year of the season (e.g., 2023).
        :return: A list of Standing objects.
        """
        params = {}
        if season:
            params['season'] = season
            
        response_data = self.client.get(f"competitions/{competition_id}/standings", params=params)
        return StandingsResponse(**response_data).standings 