# --------------------------------------------------------------------------------
# Name: RandomHuman
# Description: No description
# Author: Dorotoro & special thanks to Den4ikSOP (@AstroModules)
# Commands:
# / / / .generatehuman / / /
# ---------------------------------------------------------------------------------
#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/km90h
#             https://www.gnu.org/licenses/agpl-3.0.html                 
#                                                         
# ---------------------------------------------------------------------------------
#
# meta developer: @DorotoroMods

from .. import loader, utils
from ..utils import answer
from telethon.tl.types import Message


@loader.tds
class RandomHuman(loader.Module): 
	"""Отправляет рандомное имя, фамилию, дату рождения, email, пароль и телефон.""" 
	strings = {'name': 'RandomHuman'} 
	
	@loader.command()
	async def generatehumancmd(self, message: Message):
		"- сгенерировать человека."
		msg = await answer(message, '<b><i>Подбираю человека...</i></b>')
		async with self._client.conversation("@randomdatatools_bot") as conv:
			popo4ka = await conv.send_message("👤 Пользователь")
			r = await conv.get_response()
			await popo4ka.delete() 
			await r.delete()
		dsopthx = r.text.split('\n')
		dsopthx.remove('👤 Пользователь')
		dsopthx.remove('<i>(Нажмите на значение, чтобы скопировать его)</i>')
		chel = '\n'.join(dsopthx)
		text = f"<b>Человек сгенерирован. Кое-что про него:\n\n{chel}\n\n<tg-spoiler><i>RandomHuman</i></tg-spoiler></b>"
		await answer(msg, text)
