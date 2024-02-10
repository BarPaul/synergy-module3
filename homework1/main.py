from telebot import TeleBot, types
from config import TOKEN


bot = TeleBot(TOKEN, 'html')

@bot.message_handler(content_types=['text'])
def echo_command(message: types.Message):
    message_text = str(message.html_text + '\n') * 10
    if len(message_text) > 4090:
        return bot.reply_to(message, "Текст сообщения слишком большой!")
    bot.reply_to(message, message_text)


if __name__ == '__main__':
    bot.infinity_polling()
