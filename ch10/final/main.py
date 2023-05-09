from datetime import datetime
from espn_api import ESPNAPI
from openweathermap_api import OpenWeatherMapAPI

OWM_API_KEY = '244bad0cc58b6a739b36b1d67a0b42f3'

def main():
    espn_api = ESPNAPI()
    games = espn_api.get_games(datetime.today().strftime('%Y%m%d'))

    weather_api = OpenWeatherMapAPI(OWM_API_KEY)
    for game in games:
        venue = game['competitions'][0]['venue']
        city_name = f"{venue['city']}, {venue['state']}, {venue['country']}"
        weather = weather_api.get_weather(city_name)
        print(f"{game['shortName']}: {weather}")

if __name__ == '__main__':
    main()

