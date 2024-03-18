# Импорт нужных библиотек/пакетов
from telebot import TeleBot
from hunt import generate_reward, generate_message, convert_inventory
from seller import generate_trade
from config import *


# Записываем в переменную бота
bot = TeleBot(TOKEN, 'html')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    # Если пользователь не присутсвует в датабазе
    if db.is_new(message.from_user.id):
        # Изменение уникального ID кнопок да и нет
        YES.callback_data = "yes_start"
        # Изменение уникального ID кнопок да и нет
        NO.callback_data = "no_start"
        # Изменение текста кнопок да и нет
        YES.text, NO.text = "Да", "Нет"
        # Ответ пользователю с клавиатурой "Да Нет" и остановка функции
        return bot.reply_to(message, "👴: Приветствую тебя, путник! Не заблудился ли ты?", reply_markup=YN)
    # Если уже не новичек, отвечать, что это невозможно
    bot.reply_to(message, IMPOSSIBLE)


# Обработка кнопок главного меню
@bot.message_handler(func=lambda message: message.text in MAIN_BUTTONS)
def menu_command(message: types.Message):
    # Если пользователь "новичек", запретить пользование
    if db.is_new(message.from_user.id):
        # Завершение функции с ответом "О чем вы путник?"
        return bot.reply_to(message, "О чем вы путник?")
    # Получения инвентаря из датабазы SQLITE3
    inv = db.get_inventory(message.from_user.id)
    # Проверка текста сообщения
    if message.text == "⛏️ Пустынная охота":
        # Генерация текста для квеста
        mes = generate_message()
        # Изменение уникального ID кнопок да и нет
        NO.callback_data, YES.callback_data = mes['no'], mes['yes']
        # Изменение текста кнопок да и нет
        NO.text, YES.text = mes.get("no_text", "Нет"), mes.get("yes_text", "Да")
        # Обновление клавиатуры
        YN.keyboard[0] = [YES, NO]
        # Отправка сообщению пользователю
        bot.reply_to(message, mes['text'], reply_markup=YN)
    # Если кнопка "Торговец"
    elif message.text == "🛒 Торговец":
        # Если инвентарь пуст
        if inv is None:
            # Ответить пользователю и завершить функцию
            return bot.reply_to(message, "У тебя пока что нет предметов для обмена")
        # Генерация подходящего предложения
        data = generate_trade(inv)
        # Изменение уникального ID кнопки принять
        YES_TRADE.callback_data = f"trade_accept_{data['need_material']}_{data['need_count']}_{data['sell_material']}_{data['sell_count']}"
        # Обновление кнопки в клавиатуре
        TRADE.keyboard[0][-1] = YES_TRADE
        # Обновление кнопки в клавиатуре
        bot.reply_to(message, data['text'], reply_markup=TRADE if data['is_right'] else None)
    # Если нажата кнопка "Телефон"
    elif message.text == "📱 Телефон":
        # Если инвентарь пуст
        if inv is None:
            # Превратить None в пустой словарь
            inv = {}
        # Отправка сообщения пользователю
        bot.reply_to(message, "Тебе нужен телефон для спасения\n" + '\n'.join(
                [f'{line.split()[0]} {str(inv.get(key, 0))}/{line.split()[-1]} {"✅" if inv.get(key, 0) >= REQUIREMENTS[key] else "❌"}' 
                for line, key in zip(convert_inventory(REQUIREMENTS).split("\n"), REQUIREMENTS.keys())]
            ), reply_markup=END_MARKUP if all([REQUIREMENTS[key] <= inv.get(key, 0) for key in REQUIREMENTS.keys()]) else None
        )
    # Если нажата кнопка "Инвентарь"
    elif message.text == "🎒 Инвентарь":
        # Если инвентарь пуст
        if inv is None:
            # Сказать пользователю об этом и завершить функцию
            return bot.reply_to(message, "Инвентарь\nПуст :(")
        # Отправить сообщение с инвентарем
        bot.reply_to(message, "Инвентарь\n" + convert_inventory(inv))


# Обработка первых двух кнопок "Да" (предыстории)
@bot.callback_query_handler(func=lambda c: c.data.split('_')[0] in ['no', 'yes'] and len(c.data.split("_")) == 2)
def start_callback(call: types.CallbackQuery):
    # Если уже не новичек
    if not db.is_new(call.message.from_user.id):
        # Сказать, что это невозможно и завершить функцию
        return bot.reply_to(call.message, IMPOSSIBLE)
    # Определение переменных да или нет и в каком месте
    do, _type = call.data.split("_")
    # Определение переменных для сокращения айди сообщения и чата
    mid, cid = call.message.id, call.message.chat.id
    # Если действие нет и это на старте и к храму
    if do == "no" and _type in ['start', 'temple']:
        # Отредактировать сообщение на "вы проиграли" и завершить функцию
        return bot.edit_message_text(f"{LOSE}\nСтарик чудесным образом испарился и вы погибли от жажды, так как остались лежать на песке\n(начать игру снова /start)", cid, mid, reply_markup=None)
    # Если это на старте
    if _type == "start":
            # изменение уникального ID кнопок да и нет (для смены локации)
            NO.callback_data, YES.callback_data = "no_temple", "yes_temple"
            # Обновление клавиатуры
            YN.keyboard[0] = [YES, NO]
            # Отредактировать сообщение на продолжение
            bot.edit_message_text("👴: Пройди в пустынный храм. Он укажет тебе путь", cid, mid, reply_markup=YN)
    # Если около храма
    elif _type == "temple":
            # Отредактировать сообщение
            bot.edit_message_text("Вы вошли в древний храм. ", cid, mid, reply_markup=None)
            # Ответить пользователю сообщением с главным меню
            bot.reply_to(call.message, "Довольно странное место, но есть небольшие запасы воды, пищи и одичалый торговец", reply_markup=MAIN_MENU)
            # Добавить пользователя в датабазу
            db.insert_user(call.from_user.id)


# Обработка кнопок на охоте
@bot.callback_query_handler(func=lambda c: len(c.data.split("_")) == 3 and c.data.split("_")[0] in ['yes', 'no'])
def history_callback(call: types.CallbackQuery):
    # Определение типа, айди и само действие, также сокращение айди сообщения и чата
    [_type, tid, do], mid, cid = call.data.split("_"), call.message.id, call.message.chat.id
    # Если действие проиграть
    if do == "0":
        # Отредактировать сообщение на проиграли с причиной
        bot.edit_message_text(f"{LOSE}\n{HUNT_MESSAGES[int(tid)]['lose_text']}\n(Начать игру снова /start)", cid, mid, reply_markup=None)
        # Удалить пользователя из датабазы
        db.delete_user(call.from_user.id)
    # Если действие только сообщение
    elif do == "1":
        # Получение сообщения
        message = HUNT_MESSAGES[int(tid)][f'{_type}_response']
        # Отредактирование сообщения
        bot.edit_message_text(message, cid, mid, reply_markup=None)
    # Если действие сообщение с призом
    elif do == "2":
        # Получение сообщения
        message = HUNT_MESSAGES[int(tid)][f'{_type}_response']
        # Генерация награды
        reward = generate_reward()
        # Если награды нет
        if reward is None:
            # Редактирование сообщения с форматированием с "Ничего" и окончание функции
            return bot.edit_message_text(message.format("Ничего :("), cid, mid, reply_markup=None)
        # Редактирование сообщения с форматированием с призом
        bot.edit_message_text(message.format(convert_inventory(reward)), cid, mid, reply_markup=None)
        # Цикл для каждого предмета в награде
        for k, v in reward.items():
            # Добавить предмет в инвентарь
            db.add_item(call.from_user.id, k, v)


# Обработка кнопки "Создать телефон"
@bot.callback_query_handler(func=lambda c: c.data == "game_end")
def game_end_callback(call: types.CallbackQuery):
    # Ответ пользователю об окончании игры
    bot.reply_to(call.message, END_GAME)
    # Удаление сообщения бота о крафте
    bot.delete_message(call.message.chat.id, call.message.id)
    # Удаления пользователя из датабазы
    db.delete_user(call.from_user.id)


# Обработка кнопки "Отклонить трейд"
@bot.callback_query_handler(func=lambda c: c.data == "trade_decline")
def decline_trade(call: types.CallbackQuery):
    # Удаляем сообщение о трейде
    bot.delete_message(call.message.chat.id, call.message.id)


# Обработка кнопки "Принять трейд"
@bot.callback_query_handler(func=lambda c: c.data.startswith("trade_accept"))
def accept_trade(call: types.CallbackQuery):
    # Получаем инвентарь игрока
    inv = db.get_inventory(call.from_user.id)
    # Если инвентарь пуст
    if inv is None:
        # Отправить сообщение об этом
        return bot.reply_to(call.message, "У тебя пока что нет предметов для обмена")
    # Получения информации о нужном материале и количестве, а также о материале, который получаем из call.data
    need, need_count, sell, sell_count = call.data.split("_")[2:]
    # Если инвентарь пользователя изменился
    if int(need_count) > inv.get(need, 0):
        # Предложение более неакутально
        bot.reply_to(call.message, "Извините, предложение неактуально")
        # Удаляем сообщение и заканчиваем функцию
        return bot.delete_message(call.message.chat.id, call.message.id)
    # "Отдаем" предмет из инвентаря
    db.rem_item(call.from_user.id, need, int(need_count))
    # "Отдаем" предмет из инвентаря
    db.add_item(call.from_user.id, sell, int(sell_count))
    # Удаляем сообщение о трейде
    bot.delete_message(call.message.chat.id, call.message.id)


# Если файл запущен напрямую, а не импортируется
if __name__ == '__main__':
    # Бесконечный цикл отправки запросов и получения/отправки ответов на серверах Telegram
    bot.infinity_polling()
