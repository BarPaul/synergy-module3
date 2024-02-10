# Импортирование нужных пакетов
from telebot import TeleBot, types
from random import randint
from config import TOKEN

# Иницилизация переменной бота
bot = TeleBot(TOKEN, 'html')


# Обработчик сообщений c фильтром "если текст сообщения в нижнем регистре содержит слово рандом"
@bot.message_handler(func=lambda message: "рандом" in message.text.lower())
def random_response(message: types.Message):
    # Отправка сообщения
    bot.reply_to(message, f"Случайное число: <b>{randint(0, 100)}</b>")


# Обработчик сообщений типа текст
@bot.message_handler(content_types=['text'])
def random_response(message: types.Message):
    # Отправка сообщения
    bot.reply_to(message, message.html_text)


# Если файл открывается напрямую, а не импортируется как модуль
if __name__ == '__main__':
    # Бесконечный цикл отправки запросов на сервера Telegram и получения/отправки ответов
    bot.infinity_polling()
