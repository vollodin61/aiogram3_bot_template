import logging

from environs import Env

from aiogram import Router, Dispatcher, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage  #, Redis

from aiogram.fsm.state import State, StatesGroup

from redis import Redis

from . import format_text_html as fth


url = 'http://redis://localhost:6379/0'
url2 = 'redis://localhost:6378/1'
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)

env = Env()
env.read_env()
bot_token = env("TOKEN")
admins = list(map(lambda x: int(x), (env('ADMINS')).split(', ')))  # превращаем строку админов в список int

red = Redis()  # Как это запустить, чтоб работало!! АААА!!!!!!!!
red_storage = RedisStorage.from_url(url2)  #
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(token=bot_token, parse_mode="HTML")
# rt = Router()
# dp.include_router(rt)


class AvailableState(StatesGroup):
	pass

