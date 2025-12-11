import requests
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("API key not found. Please set it in .env")
    exit()

while True:
    city = input("Enter city name (or 'q' to quit): ").strip()
    if city.lower() == 'q':
        print("Exiting weather checker.")
        break

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print(f"City not found: {data.get('message')}\n")
        else:
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Feels like: {feels_like}°C")
            print(f"Description: {weather_desc}")
            print(f"Humidity: {humidity}%")
            print(f"Wind speed: {wind_speed} m/s\n")

    except Exception as e:
        print("Error fetching weather:", e, "\n")
