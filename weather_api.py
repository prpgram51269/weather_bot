import httpx
import os
from dotenv import load_dotenv
from logger import get_logger

logger = get_logger(__name__)

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

async def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

        if response.status_code == 404:
            logger.error('Город %s не найден', city)
            return 'Неверно указан город'

        if response.status_code != 200:
            logger.error('Ошибка при подключении к сайту %s', response.status_code)
            return "❌ Ошибка при получении погоды. Попробуйте позже."

        logger.info('Ответ получен! %s', response.status_code)

        data = response.json()

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        city_name = data["name"]

        return (f"Погода в городе {city_name}:\n"
                f"🌡 Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"☁️ {description.capitalize()}\n"
                f"💨 Ветер: {wind} м/с")