# Импортирование нужных модулей/пакетов
from telebot import TeleBot, types
from random import randint, shuffle
from config import *


# Создание переменной бота
bot = TeleBot(TOKEN, 'html')


# Обработчик сообщений команды /start
@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    # Переменная Inline клавиатуры
    keyboard = types.InlineKeyboardMarkup()
    # Определения выигрышного числа
    win_number = randint(0, 4)
    # Перемешивание чисел
    shuffle(numbers)
    # Добавление кнопок в клавиатуру
    keyboard.row(*[types.InlineKeyboardButton("🎲", callback_data=f'cube_{number}_{win_number}') for number in numbers])
    # Отправка сообщения
    bot.reply_to(message, START_TEXT.format(win_number), reply_markup=keyboard)


# Обработчик кнопок
@bot.callback_query_handler(func=lambda callback: callback.data.split("_")[0] == 'cube')
def cube_callback(call: types.CallbackQuery):
    # Получения числа кубика и выигрышного 
    number, win = call.data.split("_")[1:]
    print(number, win)
    # Получение сообщения и чата
    message, chat = call.message, call.message.chat
    # При выигрыше
    bot.edit_message_text(WIN_TEXT if number == win else LOSE_TEXT, chat.id, message.id, reply_markup=None)
    # При проигрыше
    # bot.edit_message_text(LOSE_TEXT, chat.id, message.id, reply_markup=None)


# Проверка на прямое исполнение файл (если файл импортируется, то код не выполняется)
if __name__ == '__main__':
    # Бесконечный цикл отправки запросов и получения/отправка ответа на сервера Telegram
    bot.infinity_polling()
