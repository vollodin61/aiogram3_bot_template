import asyncio
import logging
import re
from datetime import datetime

from aiogram import Bot, Dispatcher, html, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.base import BaseStorage
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, KeyboardBuilder
from aiogram.utils.formatting import as_list, as_marked_section, Bold, as_key_value, HashTag
from aiogram.utils.markdown import hide_link
from aiogram.utils.media_group import MediaGroupBuilder

from config.cfg import bot, dp, AvailableState as AvS
from commands.setter import set_commands
from handlers import def_router, cust_router, set_routers


# def setup_routers(dp: Dispatcher):

async def main():
	logging.basicConfig(level=logging.INFO)
	set_routers(dp)
	# dp.include_router(def_router)
	# dp.include_router(cust_router)
	await set_commands(bot)
	# setup_routers(dp)
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())
