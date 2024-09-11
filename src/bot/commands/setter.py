from aiogram.types import BotCommand, BotCommandScopeAllChatAdministrators


async def set_commands(bot):
	await bot.set_my_commands([
		BotCommand(command="start", description="Запустить бота"),
		BotCommand(command="help", description="Помощь"),
	])


async def set_admin_commands(bot):  # Тут должны быть статусы такие же как в БД
	await bot.set_my_commands(
			[
				BotCommand(command="command_name", description="some_description"),
			],
			scope=BotCommandScopeAllChatAdministrators()
	)