import requests
from config.settings import OPENWEATHER_API_KEY, CITY

def get_weather() -> str:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": CITY,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "es"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return "No pude obtener el clima en este momento."

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    return (
        f"En {CITY} hay {description}. "
        f"Temperatura: {temp:.0f}°C, sensación térmica {feels_like:.0f}°C, "
        f"humedad {humidity}%."
    )