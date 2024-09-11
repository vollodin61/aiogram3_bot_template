from aiogram.filters import BaseFilter
from aiogram.types import Message
from typing import Iterable


class CheckRole(BaseFilter):
	"""TODO тут почему-то при создании экземпляра фильтра должен передаваться список ids
	Не должно быть такого, он должен быть сюда импортирован, наверное, из конфига
	TODO либо этот переделать, либо новый написать"""
	def __init__(self, user_ids: int | Iterable) -> None:
		self.user_ids = user_ids

	async def __call__(self, msg: Message) -> bool:
		if isinstance(self.user_ids, int):
			return msg.from_user.id == self.user_ids
		return msg.from_user.id in self.user_ids
