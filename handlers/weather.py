from aiogram import types
from aiogram.fsm.context import FSMContext

from db import db
from states import Weather
from weather_api import get_weather


# 1 кнопка
async def city_weather(message: types.Message, state: FSMContext):
    await message.answer('Напишите название своего города.')
    await state.set_state(Weather.city_name)

async def name_city(message: types.Message, state: FSMContext, user_id: int):
    city = message.text.strip()
    response = await get_weather(city)
    await message.answer(response)
    await state.clear()
    await db.add_users(user_id, city)
    await db.add_weather_history(user_id, city)

# 2 кнопка
async def weather_in_city(message: types.Message, user_id: int):
    city = await db.get_user_city(user_id)
    if city:
        response = await get_weather(city)
        await message.answer(response)
        await db.add_weather_history(user_id, city)
    else:
        await message.answer('Для начала укажите свой город')
