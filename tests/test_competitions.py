import pytest
import requests_mock
from football_data import FootballData
from football_data.models.competition import Competition

@pytest.fixture
def sdk():
    return FootballData(api_key="fake-key")

def test_get_all_competitions(sdk, requests_mock):
    mock_response = {
        "count": 1,
        "filters": {},
        "competitions": [
            {
                "id": 2021,
                "name": "Premier League",
                "code": "PL",
                "type": "LEAGUE",
                "emblem": "https://crests.football-data.org/PL.png",
                "area": {
                    "id": 2072,
                    "name": "England",
                    "code": "ENG",
                    "flag": "https://crests.football-data.org/770.svg"
                }
            }
        ]
    }
    requests_mock.get("https://api.football-data.org/v4/competitions", json=mock_response)
    
    competitions = sdk.competitions.get_all()
    
    assert len(competitions) == 1
    assert isinstance(competitions[0], Competition)
    assert competitions[0].name == "Premier League"
    assert competitions[0].area.name == "England"
