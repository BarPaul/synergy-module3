# Импортирование нужных библиотек
from telebot import TeleBot, types
from courses import get_courses
from config import TOKEN, COURSES_PER_COMMAND
from difflib import SequenceMatcher as match


# Создание переменных ботов
bot = TeleBot(TOKEN, 'markdown')


# Обработка сообщений схожих с сообщением "курсы" на 50% или же команды start, course, courses
@bot.message_handler(func=lambda message: match(a=message.text.lower(), b="курсы").ratio() >= 0.5)
@bot.message_handler(commands=['start', 'course', 'courses'])
def course_command(message: types.Message):
    # Получение случайных курсов к рублю
    reply_text = '\n'.join(map(str, get_courses(COURSES_PER_COMMAND)))
    # Ответ пользователю
    bot.reply_to(message, reply_text)


# Если файл запущен напрямую, а не импортируется
if __name__ == '__main__':
    # Бесконечный цикл отправки запросов и получения/отправки ответов на сервера Telegram
    bot.infinity_polling()
