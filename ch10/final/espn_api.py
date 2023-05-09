import requests

class ESPNAPI:
    api_url = 'https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard'

    def __init__(self):
        self.games = []

    def get_games(self, date):
        params = {
            'lang': 'en',
            'region': 'us',
            'calendartype': 'blacklist',
            'limit': '1000',
            'dates': date
        }
        response = requests.get(self.API_URL, params=params)
        data = response.json()
        self.games = data['events']
        return self.games
