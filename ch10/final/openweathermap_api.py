import requests

class OpenWeatherMapAPI:
    api_url = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city_name):
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.API_URL, params=params)
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return f"{temperature}°C and {weather_description}"
