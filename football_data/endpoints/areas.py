from typing import List
from football_data.client import APIClient
from football_data.models.area import Area, AreasResponse

class Areas:
    def __init__(self, client: APIClient):
        self.client = client

    def get_all(self) -> List[Area]:
        """
        List all available areas.
        """
        response_data = self.client.get("areas")
        return AreasResponse(**response_data).areas
    
    def get_one(self, area_id: int) -> Area:
        """
        Get a single area by its ID.
        :param area_id: The ID of the area.
        :return: An Area object.
        """
        response_data = self.client.get(f"areas/{area_id}")
        return Area(**response_data) 