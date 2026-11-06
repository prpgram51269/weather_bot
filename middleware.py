from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message


class RoleMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, (Message, CallbackQuery)):
            user = event.from_user
        else:
            return await handler(event, data)

        data['user_id'] = user.id
        return await handler(event, data)