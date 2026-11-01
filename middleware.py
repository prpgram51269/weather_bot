from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

class RoleMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            user = event.from_user
        elif isinstance(event, CallbackQuery):
            user = event.from_user
        else:
            return await handler(event, data)

        data['user_id'] = user.id
        return await handler(event, data)