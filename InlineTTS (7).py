
# ---------------------------------------------------------------------------------
# Name: SileroTTS
# Description: No description
# Author: Dorotoro & code-fixer @Den4ikSuperOstryyPer4ik
# Commands:
# .silerotts 
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
# 						Copyright 2022 t.me/km90h
#             https://www.gnu.org/licenses/agpl-3.0.html 
#
# meta developer: Dorotoro & @Den4ikSuperOstryyPer4ik

import re 
from .. import loader, utils
from telethon.tl.types import Message
 
@loader.tds 
class InlineTTS(loader.Module): 
	"""Перед началом работы с модулем необходимо решить каптчу в боте @Silero_Voice_Bot, иначе модуль работать не будет. Также пишите имя героя с МАЛЕНЬКОЙ буквы, иначе тоже будет выбивать ошибку. Также (из-за бота) английские символы не поддерживаются."""
	
	strings = {"name": "InlineTTS"}

	
	@loader.command()
	async def silerotts(self, message: Message):
		"<герой> <ваш текст> - синтезирует текст в голос героев из Warcraft III и обычных говорилок."
		args = utils.get_args_raw(message)
		reply = await message.get_reply_message()
		async with self._client.conversation("@silero_voice_bot") as conv:
			await conv.send_message(args) 
			r = await conv.get_response()
		await message.respond(file=r, reply_to=reply.id if reply else None)
		if message.out:
			await message.delete()

	@loader.command()
	async def warcraftvoices(self,m):
		"- всевозможные голоса для синтеза (Герои Warcraft III)"
		await m.edit(" 💬 Warcraft III Voices  <code> Arthas </code>| <code>  Kelthuzad </code>| <code>  Anubarak </code> | <code>  Thrall </code> | <code>  Grunt </code> | <code>  Cairne </code> | <code>  Rexxar </code> | <code>  Uther </code> | <code> Jaina </code> | <code>  Kael  | <code> Garithos </code> | <code>  Malev </code> | <code>  Naisha </code> | <code> Tyrande </code> | <code> Furion </code> | <code>  Illidan </code> | <code>  Ladyvashj </code> | <code>  Narrator </code> | <code>  Medivh </code> | <code>  Villagerm </code> ")

	@loader.command()
	async def silerovoices(self,m):
		"- всевозможные голоса для синтеза (Обычные голоса Silero)"
		await m.edit("👾 Silero Voices: <code> Aidar </code> | <code> Baya </code> | <code> Kseniya </code> | <code> Xenia </code> | <code> Eugene </code>")