from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def weather_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Указать город')],
            [KeyboardButton(text='Узнать погоду в городе')]
        ]
    )