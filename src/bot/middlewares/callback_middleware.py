from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import TelegramObject, CallbackQuery


class CallbackMiddleware(BaseMiddleware):
    def __init__(self, storage: RedisStorage):
        self._storage = storage

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        print("callback middleware not enable, but working")
        return await handler(event, data)
