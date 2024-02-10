# Импортирование нужных модулей
from telebot import TeleBot, types
from weather import get_weather, get_weather_code
from config import *


# Определение переменной бота
bot = TeleBot(TOKEN, 'html')


# Функция, которая выполняется после ожидания сообщения
def next_step_weather(message: types.Message):
    # Если отправлена не геопозиция
    if message.content_type != 'location':
        # Отправить сообщение
        bot.reply_to(message, "Пришлите пожалуйста свое местоположение (геопозицию)")
        # Возращаем обратно функцию, т. е. опять запрашиваем геопозицию
        return bot.register_next_step_handler_by_chat_id(message.chat.id, next_step_weather)
    # Получение погоды из функции
    wea = get_weather(message.location.latitude, message.location.longitude)
    # Если погода это строка, то значит там ошибка
    if isinstance(wea, str):
        # Отправка сообщения об ошибке и окончание функции
        return bot.reply_to(message, "Извините, технические неполадки.")
    # Форматирование даты
    [yyyy, mm, dd], time = wea.time.split("T")[0].split("-"), wea.time.split("T")[1]
    # Отправка сообщения
    bot.reply_to(message, WEATHER_INFO.format(f"{'.'.join([dd, mm, yyyy])} {time}", 
                                            wea.temperature_2m, 
                                            wea.apparent_temperature, 
                                            wea.relative_humidity_2m, 
                                            wea.cloud_cover, 
                                            wea.wind_speed_10m,
                                            get_weather_code(wea.weather_code)
                        )
    )


# Обработка команды /weather
@bot.message_handler(commands=['weather'])
def weather_command(message: types.Message):
    # Отправка сообщения
    bot.reply_to(message, SEND_PLEASE)
    # Ожидание ответа на сообщение
    bot.register_next_step_handler_by_chat_id(message.chat.id, next_step_weather)


# Если запущен код от файла, а не импортирован
if __name__ == '__main__':
    # Бесконечный цикл запросов и отправка/получение ответов на серверах Telegram
    bot.infinity_polling()
