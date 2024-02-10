# Импортирование нужных пакетов
from telebot import TeleBot, types
from config import TOKEN


# Создание переменной бота
bot = TeleBot(TOKEN, 'html')


# Обработчик всех сообщений типа текст
@bot.message_handler(content_types=['text'])
def poll_creation(message: types.Message):
    # Деление сообщения на строки
    lines = message.text.split("\n")
    # Если количество строк меньше 3 или больше 11, прислать сообщение и закончить выполнение функции
    if len(lines) < 3 or len(lines) > 11:
        return bot.reply_to(message, "<b>Ошибка</b>\nКоличество строк должно быть от <b>3</b> до <b>11</b>!")
    # Отправка опроса, после валидации данных
    bot.send_poll(message.chat.id, lines[0], lines[1:])


# Если запуск файла идет напрямую, а не через импорт
if __name__ == '__main__':
    # Бесконечный цикл отправки запросов и получения/отправки ответов на сервера Telegram
    bot.infinity_polling()
