from dataclasses import dataclass

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from environs import Env

from src.bot.config.redis_connection import Singleton


@dataclass
class SellerConfig:
    env = Env()
    env.read_env()
    bot_token = env("TOKEN")
    redis_host = env("REDIS_HOST")
    redis_port = env("REDIS_PORT")

    red = Singleton.get_connection(host=redis_host, port=redis_port)
    dp = Dispatcher(storage=red_storage)
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode='HTML'))


