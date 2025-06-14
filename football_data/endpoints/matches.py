from typing import List, Optional
from football_data.client import APIClient
from football_data.models.match import Match, MatchResponse
from datetime import date

class Matches:
    def __init__(self, client: APIClient):
        self.client = client

    def get_all(
        self,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        status: Optional[str] = None,
        competitions: Optional[List[str]] = None,
        matchday: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List[Match]:
        """
        Get matches based on filters.
        """
        params = {}
        if date_from:
            params['dateFrom'] = date_from.isoformat()
        if date_to:
            params['dateTo'] = date_to.isoformat()
        if status:
            params['status'] = status
        if competitions:
            params['competitions'] = ",".join(competitions)
        if matchday:
            params['matchday'] = matchday
        if limit:
            params['limit'] = limit

        response_data = self.client.get("matches", params=params)
        return MatchResponse(**response_data).matches

    def get_one(self, match_id: int) -> Match:
        """
        Get a single match by its ID.
        :param match_id: The ID of the match.
        :return: A Match object.
        """
        response_data = self.client.get(f"matches/{match_id}")
        return Match(**response_data)
