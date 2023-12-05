from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from bot.data.smiles import Texts as Txt
from bot.config.cfg import bot, admins


cust_router = Router()

@cust_router.message()
async def any_message(msg: Message, bot: bot):
	try:
		await msg.answer(Txt.echo_text, parse_mode=ParseMode.HTML)
	except Exception as exc:
		await bot.send_message(chat_id=admins[0], text=exc)
