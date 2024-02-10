# Импортирование нужных модулей
from telebot import TeleBot, types
from config import TOKEN, URL, BROKEN_URL
from requests import get, exceptions


# Создание переменной бота
bot = TeleBot(TOKEN)


# Обработчик сообщений с командой /coffee
@bot.message_handler(commands=['coffee'])
def coffee_command(message: types.Message):
    # Конструкция try/except для вылавливания ошибок во время запроса
    try:
        # Отправка запроса на сервер, кодирование в JSON объект и получения ключа file (в нем ссылка на фото)
        photo_url = get(URL).json().get('file', BROKEN_URL)
        # Отправка фотографии пользователю
        bot.send_photo(message.chat.id, photo_url)
    except exceptions.JSONDecodeError:
        # Если запрос вернул неожиданный результат, то прислать фотографию "ничего не найдено" 
        bot.send_photo(message.chat.id, BROKEN_URL)


# Если файл запускается на прямую, а не импортируется
if __name__ == '__main__':
    # Бесконечный цикл отправки запросов и получения/отправки ответов на сервера Telegram
    bot.infinity_polling()
