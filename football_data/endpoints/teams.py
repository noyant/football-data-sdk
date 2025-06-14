from typing import List, Optional
from football_data.client import APIClient
from football_data.models.team import Team, CompetitionTeamResponse, AllTeamsResponse

class Teams:
    def __init__(self, client: APIClient):
        self.client = client

    def get_all(self, limit: Optional[int] = None) -> List[Team]:
        """
        Get all available teams.
        :param limit: The number of teams to return.
        :return: A list of Team objects.
        """
        params = {}
        if limit:
            params['limit'] = limit
        
        response_data = self.client.get("teams", params=params)
        return AllTeamsResponse(**response_data).teams

    def get_for_competition(self, competition_id: int, season: Optional[int] = None, stage: Optional[str] = None) -> List[Team]:
        """
        Get all teams for a given competition.
        :param competition_id: The ID of the competition.
        :param season: The starting year of the season (e.g., 2023).
        :param stage: The stage of the competition.
        :return: A list of Team objects.
        """
        params = {}
        if season:
            params['season'] = season
        if stage:
            params['stage'] = stage
            
        response_data = self.client.get(f"competitions/{competition_id}/teams", params=params)
        return CompetitionTeamResponse(**response_data).teams

    def get_one(self, team_id: int) -> Team:
        """
        Get a single team by its ID.
        :param team_id: The ID of the team.
        :return: A Team object.
        """
        response_data = self.client.get(f"teams/{team_id}")
        return Team(**response_data)
