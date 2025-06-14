from typing import List, Optional
from football_data.client import APIClient
from football_data.models.competition import Competition, CompetitionResponse

class Competitions:
    def __init__(self, client: APIClient):
        self.client = client

    def get_all(self, area_ids: Optional[List[int]] = None, plan: Optional[str] = None) -> List[Competition]:
        """
        Get all available competitions.
        :param area_ids: List of area IDs to filter competitions.
        :param plan: The plan to filter competitions (e.g., TIER_ONE).
        :return: A list of Competition objects.
        """
        params = {}
        if area_ids:
            params['areas'] = ",".join(map(str, area_ids))
        if plan:
            params['plan'] = plan
        
        response_data = self.client.get("competitions", params=params)
        competition_response = CompetitionResponse(**response_data)
        return competition_response.competitions

    def get_one(self, competition_id: int) -> Competition:
        """
        Get a single competition by its ID.
        :param competition_id: The ID of the competition.
        :return: A Competition object.
        """
        response_data = self.client.get(f"competitions/{competition_id}")
        return Competition(**response_data)
