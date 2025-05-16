# Weather program python project

import requests
from pprint import pprint

API_KEY = "411cc9c1cf36b2479d10749826564a7f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    # Construct the complete API URL
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    
    # Send a GET request to the OpenWeatherMap API
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        # If the request was successful, return the weather data
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "clouds": data["clouds"]["all"],
            "wind_speed": data["wind"]["speed"],
        }
    else:
        # If the request failed, return an error message
        print(f"error: {data.get('message', 'City not found')}")
    
if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    weather = get_weather(city_name)
    if weather:
        pprint(weather)