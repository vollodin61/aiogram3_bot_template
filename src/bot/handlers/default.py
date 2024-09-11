from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


def_router = Router()


@def_router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
	await message.answer(text='Приветствую!')
