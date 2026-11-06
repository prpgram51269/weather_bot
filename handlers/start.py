from aiogram import types

from keyboards import weather_kb


async def first_message(message: types.Message):
    await message.answer('Этот бот поможет вам узнать погоду в вашем городе. Нажмите кнопку снизу', reply_markup=weather_kb())