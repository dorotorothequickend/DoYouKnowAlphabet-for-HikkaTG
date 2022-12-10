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
# meta banner: https://0x0.st/ody0.gif.mp4
# meta developer: @DorotoroMods

from .. import utils, loader
import random

@loader.tds
class ExcuseGeneratorMod(loader.Module):
    strings = {
        "name": "Генератор Отмазок"
        }

    @loader.command()
    async def excuse(self, message):
        """<имя> - генерирует отмазку."""
        args = utils.get_args_raw(message)
        nameo = [
        "Друг","Товарищ","Заказчик",
        "Приятель","Уважаемый начальник", "Дорогой друг", "Мой лучший друг", 
        "Пупсик"
        ]
        hello = [
        "привет","здравствуй","приветствую","добрый день","добрый вечер",
        "доброе утро","саламули гамаджоба", "хорошего дня",
        "салам алейкум", "hello", "здарова", "алоха"
        ]
        fail = [
        "Самолет, в котором я летел, приземлился на запаснике в Новгороде",
        "Я ехал в поезде, и кто-то сорвал стопкран, я резко упал и ударился головой, сейчас в больнице",
        "Я поймал попутку, её остановила ГИБДД, и нашли крупную партию наркотиков. Сейчас я под следствием",
        "Я вышел из дома, а дверь захлопнулась, я попытался залезть через балкон, но упал. Сейчас я в травмпункте, иду на поправку",
        "Я шел по парку, и на меня напал бомж, он украл у меня кошелек и ключи от дома. Хорошо, хоть что не изнасиловал",
        "У меня развалилась кровать во время сна, я повредил позвоночник. Сейчас иду на поправку","Я потерял паспорт",
        "Я на похоронах был, последний дедушка умер","У меня рак нашли, я по больницам ездил",
        "У меня рак печени, к сожалению, серьезно, я сейчас химиотерапию прохожу","Я потерял всё, что было в портмоне",
        "Меня избили цыгане", "У меня котик умер, я на похоронах ", "Я в аэропорту, меня депортировали ", "Сломал ногу. Меня положили в больницу, восстанавливаюсь "
        "Я просто в глуши был","Я просто был не в городе","Меня отправили по делам","Твой банк отклонил перевод","Мой счет заблокировали",
        "Я потерял ноутбук","У меня сломался компьютер", "Компьютер взорвался, починю и всё сделаю", "У меня передозировка кофеина. Я в больнице "
        "Меня машина сбила","Я немного не успеваю","Я сейчас работаю по фрилансу","Скоро стартап окупится","Бабушка скоро пенсию получит",
        "Деньги вернул твой банк, пишет отказ, проверь номер карты","Платеж на обработке","Платеж отклонен, буду ругаться с банком",
        "Провожаю слепую бабушку через дорогу","Сломал позвоночник", "Мои рыбки всплыли наверх, скоро похороны", "Я ослеп", "Около моего дома убили девушку, сейчас всех опрашивают "
        "Меня в армию забрали","У меня кошка рожала","У меня дочь родила",
        "У меня молоко убежало","У меня квартира сгорела","Я недооценил задачу","Я недооценил масштаб задачи",
        "Я столкнулся с непредвиденными сложностями"
        ]
        action = [
        "Я сделаю всё","Вышлю часть","Постараюсь","Доберусь и всё сделаю","Смогу сделать всё","Я закончу","Я доделаю","Я исправлю","Согласую всё",
        "Объясню всё подробнее","Смогу отослать","Смогу решить этот вопрос","Смогу доделать","Смогу закончить",
        "Сделаю перевод","Переведу","Приеду","Я лично встречусь с тобой","Я разберусь с этим","Я разгребу это","Решу всё","Отправлю",
        "Скину","Доеду до дома","Приеду домой","Закрою этот вопрос","Попробую","Давай встретимся","Давай наличкой отдам", "Как-нибудь позже", "Может быть потом", 
        "Всё сделаю", "Еду из армии", "Чиню компьютер"
        ]
        date = [
        "сейчас","завтра","завтра вечером","завтра днем","завтра утром","как можно быстрее",
        "как можно скорее","наконец-то","чуть позже","позже","около 2 суток","в конце недели",
        "в конце месяца","в конце дня","до конца следующей недели","до завтра","послезавтра","ближе к вечеру",
        "ближе к утру","с утра","завтра крайний срок","на неделе",
        "через пару дней","скоро","сразу","сейчас, в течение 3-4 дней"
        ]
        general = [
        "Хочу закрыть вопрос поскорее","Сам уже устал ждать","Я бы с радостью уже все сделал","Сам в шоке, что так всё получилось",
        "Сам в шоке, что так всё затягивается","Сам не ожидал таких событий","Надо поскорее решить этот вопрос",
        "Надо уже закрыть этот вопрос",
        "Надо уже решить эту проблему","Я, конечно, очень извиняюсь, что так вышло"]
        rnh = random.choice(hello)
        rnf = random.choice(fail)
        rna = random.choice(action)
        rnd = random.choice(date)
        rng = random.choice(general)
        if not args:
            args = random.choice(nameo)
        await utils.answer(message, f"<b>{args}, {rnh}! {rnf}. {rna} {rnd}. {rng}.</b>")
