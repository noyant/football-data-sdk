from football_data.client import APIClient
from football_data.models.person import Person

class Persons:
    def __init__(self, client: APIClient):
        self.client = client
    
    def get_one(self, person_id: int) -> Person:
        """
        Get a single person by their ID.
        :param person_id: The ID of the person.
        :return: A Person object.
        """
        response_data = self.client.get(f"persons/{person_id}")
        return Person(**response_data) 