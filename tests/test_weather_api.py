import respx
from httpx import Response
from weather_api import get_weather

FAKE_JSON = {
    "main": {"temp": 10.5, "feels_like": 8.0},
    "weather": [{"description": "пасмурно"}],
    "wind": {"speed": 3.5},
    "name": "Moscow"
}

@respx.mock
async def test_weather_api():
    respx.get('https://api.openweathermap.org/data/2.5/weather').mock(return_value=Response(200, json=FAKE_JSON))

    result = await get_weather('Moscow')

    assert "10.5" in result
    assert "8.0" in result
    assert "3.5" in result
    assert "Moscow" in result

@respx.mock
async def test_get_weather_city_not_found():
    respx.get("https://api.openweathermap.org/data/2.5/weather").mock(return_value=Response(404))
    result = await get_weather("Nongrad")
    assert "Неверно указан город" in result