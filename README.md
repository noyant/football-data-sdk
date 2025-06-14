# football-data-sdk

A python based SDK to interact with the [football-data.org API](https://www.football-data.org/).

This SDK provides a fully-typed, idiomatic Python interface for the football-data.org API, making it easy to integrate football data into your projects.

## Installation

```bash
pip install football-data-sdk
```

You will also need to install the development dependencies if you want to run tests or contribute:

```bash
pip install "football-data-sdk[dev]"
```

## Configuration

The SDK requires an API key from football-data.org. You can get one by registering on their website.

Once you have your key, you can provide it to the SDK in one of two ways:

1.  **Environment Variable (recommended):**

    Create a `.env` file in your project root and add the following line:

    ```
    FOOTBALL_DATA_API_KEY="YOUR_API_KEY"
    ```

    The SDK will automatically load this using `python-dotenv`.

2.  **Directly in code:**

    You can pass the API key when initializing the client:

    ```python
    from football_data import FootballData

    sdk = FootballData(api_key="YOUR_API_KEY")
    ```

## Usage

Here's a quick example of how to use the SDK:

```python
from football_data import FootballData

# Initializes the SDK. It will look for the API key in your .env file.
sdk = FootballData()

try:
    # Get all competitions for England (Area ID 2072)
    print("Fetching English competitions...")
    competitions = sdk.competitions.get_all(area_ids=[2072])
    for competition in competitions:
        print(f"- {competition.name} (Code: {competition.code})")

    # Get teams from the Premier League (ID 2021)
    print("\nFetching Premier League teams...")
    pl_teams = sdk.teams.get_for_competition(2021)
    for team in pl_teams:
        print(f"- {team.name} ({team.tla})")

    # Get today's scheduled matches
    print("\nFetching today's scheduled matches...")
    matches = sdk.matches.get_all(status='SCHEDULED')
    if matches:
        for match in matches:
            home = match.homeTeam.shortName or match.homeTeam.name
            away = match.awayTeam.shortName or match.awayTeam.name
            print(f"- {home} vs {away} at {match.utcDate.strftime('%H:%M')} UTC")
    else:
        print("No scheduled matches today.")

except Exception as e:
    print(f"An error occurred: {e}")
```

## Running Tests

To run the tests, first install the dev dependencies, then run pytest:

```bash
pip install "football-data-sdk[dev]"
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
