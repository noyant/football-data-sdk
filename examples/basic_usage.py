from football_data import FootballData
import os

# Load the API key from .env file (make sure it's created and has the key)
# Or, you can pass it directly: FootballData(api_key="YOUR_API_KEY")
sdk = FootballData()

try:
    # Get all competitions
    print("Fetching competitions...")
    competitions = sdk.competitions.get_all(area_ids=[2072]) # English competitions
    for competition in competitions:
        print(f"- {competition.name} ({competition.code})")
    
    # Get teams from the Premier League
    print("\nFetching Premier League teams...")
    pl_teams = sdk.teams.get_for_competition(2021) # 2021 is the ID for the Premier League
    for team in pl_teams:
        print(f"- {team.name} ({team.tla})")

    # Get today's matches
    print("\nFetching today's matches...")
    matches = sdk.matches.get_all()
    if matches:
        for match in matches:
            print(f"- {match.homeTeam.name} vs {match.awayTeam.name} ({match.status})")
    else:
        print("No matches today.")

except Exception as e:
    print(f"An error occurred: {e}")
