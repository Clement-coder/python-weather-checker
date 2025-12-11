import requests

# Get your free API key from https://openweathermap.org/api
API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ").strip()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print(f"City not found: {data.get('message')}")
    else:
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
except Exception as e:
    print("Error fetching weather:", e)
