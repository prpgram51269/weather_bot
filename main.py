from config import PROXY, BOT_TOKEN
from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import Command
import asyncio
from aiogram import F
from aiogram.filters import StateFilter

from handlers.start import first_message
from middleware import RoleMiddleware
from handlers.weather import city_weather, name_city, weather_in_city
from states import Weather
from db import db


session = AiohttpSession(proxy=PROXY)
bot = Bot(token=BOT_TOKEN, session=session)

dp = Dispatcher()

async def main():
    await db.connect()

    dp.message.middleware(RoleMiddleware())
    dp.callback_query.middleware(RoleMiddleware())

    dp.message.register(first_message, Command('start'))
    dp.message.register(city_weather, F.text=='Указать город')
    dp.message.register(name_city, StateFilter(Weather.city_name))
    dp.message.register(weather_in_city, F.text=='Узнать погоду в городе')
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())