# ---------------------------------------------------------------------------------
# Name: InlineTTS
# Description: No description
# Author: Dorotoro & code-fixer @Den4ikSuperOstryyPer4ik
# Commands:
# / / / .stts / / / .wacraftvoices / / / .silerovoices / / / .halflifevoices / / / .portalvoices / / / .starcraftvoices / / / .stalkervoices / / /
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
# meta developer: @DorotoroMods

from .. import loader, utils
from telethon.tl.types import Message
 
@loader.tds 
class InlineTTS(loader.Module): 
	"""Перед началом работы с модулем необходимо решить каптчу в боте @Silero_Voice_Bot, иначе модуль работать не будет. Английские символы не поддерживаются. Советы:\n\nАббревиатуры необходимо писать вот так - ЭСЭСЭСЭР\nУдарение надо ставить вот так - удар+ение"""
	strings = {"name": "InlineTTS"}

	
	@loader.command()
	async def stts(self, message: Message):
		"<герой> <ваш текст> - синтезирует текст в голос героев из Warcraft III и обычных говорилок."
		args = utils.get_args_raw(message)
		if not args:
			await utils.answer(message, "<b><emoji document_id=6327716471849878717>😱</emoji> | Чел... я пустоту не озвучиваю.</b>")
			return
		reply = await message.get_reply_message()
		async with self._client.conversation("@silero_voice_bot") as conv:
			await conv.send_message(args)
			r = await conv.get_response()
			my_msg = await conv.send_message(args)
		if r.text != 'Введите код на фото.': 
			await r.delete()
			await my_msg.delete()
		await message.respond(file=r, reply_to=reply.id if reply else None)
		if message.out:
			await message.delete()

	@loader.command()
	async def warcraftvoices(self, message):
		"- всевозможные голоса для синтеза (Герои Warcraft III)"
		await utils.answer(message, " 💬 Warcraft III Voices:\n\n<code> arthas </code>| <code>  kelthuzad </code>| <code>  anubarak </code> | <code>  thrall </code> | <code>  grunt </code> | <code>  cairne </code> | <code>  rexxar </code> | <code>  uther </code> | <code> jaina </code> | <code>  kael  | <code> garithos </code> | <code>  malev </code> | <code>  naisha </code> | <code> tyrande </code> | <code> furion </code> | <code>  illidan </code> | <code>  ladyvashj </code> | <code>  narrator </code> | <code>  medivh </code> | <code>  villagerm </code> | <code> acolyte </code> | <code> sylvanas </code> | <code> dread_bm </code> | <code> dread_t </code> | <code> illidan_f </code> | <code> mannoroth </code> | <code> muradin </code> | <code> peasant </code> | <code> priest </code> | <code> sorceress </code> | <code> preon </code> | <code> chen </code>")

	@loader.command()
	async def silerovoices(self, message):
		"- всевозможные голоса для синтеза (Обычные голоса Silero)"
		await utils.answer(message, "👾 Silero Voices:\n\n<code> aidar </code> | <code> baya </code> | <code> kseniya </code> | <code> xenia </code> | <code> eugene </code>")

	@loader.command()
	async def halflifevoices(self, message):
		"- всевозможные голоса для синтеза (Новые голоса Half-Life)"
		await utils.answer(message, "🔫 Half-Life Voices:\n\n<code> alyx </code> | <code> breen </code> | <code> gman_e2 </code> | <code> father </code> | <code> barney </code> | <code> gman </code> | <code> kleiner </code> | <code> vort_e2 </code> | <code> vort </code>")

	@loader.command()
	async def portalvoices(self, message):
		"- всевозможные голоса для синтеза (Новые голоса Portal 2)"
		await utils.answer(message, "🔮 Portal 2 Voices:\n\n <code> glados </code> | <code> wheatley </code>")

	@loader.command()
	async def starcraftvoices(self, message):
		"- всевозможные голоса для синтеза (Новые голоса Starcraft)"
		await utils.answer(message, "🪅 Starcraft Voices:\n\n<code> hanson </code> | <code> kerrigan </code> | <code> stetmann </code> | <code> tosh </code> | <code> hill </code> | <code> raynor </code> | <code> swann </code> | <code> tychus </code> | <code> valerian </code>")

	@loader.command()
	async def stalkervoices(self, message):
		"- всевозможные голоса для синтеза (Новые голоса STALKER)"
		await utils.answer(message, "🛖 Stalker Voices:\n\n<code>bandit</code>")