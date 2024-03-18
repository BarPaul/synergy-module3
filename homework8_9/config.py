# Нужные импорты
from database import Database
from telebot import types


TOKEN = "" # Вставьте тут токен
db = Database() # Иницилизация датабазы
YES = types.InlineKeyboardButton(text='Да', callback_data="yes") # Кнопка да
NO = types.InlineKeyboardButton(text='Нет', callback_data="no") # Кнопка нет
YN = types.InlineKeyboardMarkup() # Клавиатура Да или Нет
YN.row(YES, NO) # Добавление кнопок в клавиатуру
YES_TRADE, NO_TRADE = types.InlineKeyboardButton(text='✅ Принять', callback_data="trade_accept"), types.InlineKeyboardButton(text='❌ Отклонить', callback_data="trade_decline") # Кнопки принять или отклонить трейд
TRADE = types.InlineKeyboardMarkup() # Клавиатура трейда
TRADE.row(NO_TRADE, YES_TRADE) # Добавление кнопок в клавиатуру
MAIN_BUTTONS = ['⛏️ Пустынная охота', '📱 Телефон', '🛒 Торговец', '🎒 Инвентарь'] # Кнопки главного меню
MAIN_MENU = types.ReplyKeyboardMarkup() # Клавиатура главного меню
MAIN_MENU.add(*MAIN_BUTTONS) # Добавление кнопок в клавиатуру
IMPOSSIBLE = "Путник, это действие <b>невозможно</b>!" # Сообщение, когда действие невозможно
HUNT_MESSAGES = [ # Сообщения на охоте
    # По шаблону
    # {
    #     "text": "текст самой охоты",
    #     "yes": "yes_порядковыйайди_типдействия"
    #     "no": "no_порядковыйайди_типдействия"
    #     "yes_response": "сообщение, после нажатия кнопки yes"
    #     "no_response": "сообщение, после нажатия кнопки no"
    #     # Необязательные параметры
    #     "lose_text": "сообщение из-за чего проигрыш" только если одна и более кнопок ведут к проигрышу
    #     "no_text": "текст кнопки "Нет"" по умолчанию Нет
    #     "yes_text": "текст кнопки "Да"" по умолчанию Да
    #     # Как вставить текст о награде? Просто написать {} (дальше в коде отформатируется)
    # },
    {
        "text": "Вы брели по пустыне и нашли подозрительный люк. Зайти внутрь?",
        "yes": "yes_0_2",
        "no": "no_0_1",
        "yes_response": "В люке вы нашли:\n{}",
        "no_response": "Вы прошли мимо."
    },
    {
        "text": "Вы увидели погибающее животное. Что сделать?",
        "yes": "yes_1_1",
        "no": "no_1_2",
        "yes_text": "Спасти",
        "no_text": "Подождать",
        "yes_response": "Вы спасли животное.",
        "no_response": "Животное погибло. Вы получили с него:\n{}"
    },
    {
        "text": "Вас мучает жажда, рядом неизвестное озеро. Попить из него?",
        "yes": "yes_2_1",
        "no": "no_2_0",
        "lose_text": "Вы погибли от жажды.",
        "yes_response": "Вы попили из озера. Жажда восстановлена"
    },
    {
        "text": "На вас напал дикий кабан. Что сделать?",
        "yes": "yes_3_0",
        "no": "no_3_1",
        "yes_text": "Убить",
        "no_text": "Убежать",
        "lose_text": "Вы были убиты кабаном",
        "no_response": "Вы убежали от кабана."
    },
    {
        "text": "Вы нашли шахту. Посмотрим внутрь?",
        "yes": "yes_4_2",
        "no": "no_4_1",
        "yes_response": "Вы получили:\n{}",
        "no_response": "Вы прошли мимо."
    }
]
LOSE = "<b>❌ Вы проиграли!</b>" # Сообщение о проигрыше
REQUIREMENTS = { # Требования к рецепту телефона
    # По шаблону
    # "материал": количество
    "meat": 1,
    "water": 20,
    "copper": 20,
    "iron": 10,
    "gold": 5,
    "glass": 15
}
END_MARKUP = types.InlineKeyboardMarkup() # Клавиатура окончания игры
END_MARKUP.add(types.InlineKeyboardButton('Собрать телефон', callback_data="game_end")) # Добавление кнопки "Собрать телефон" в клавиатуру
END_GAME = "Вы успешно вернулись домой и рассказали всем о своей невероятной истории...\n(Игру можно начать снова /start)" # Сообщение о успешном прохождении игры