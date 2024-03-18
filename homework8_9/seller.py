# Импортирование нужных модулей/пакетов
from items import ITEMS, COURSES
from random import choice, randint
from sys import setrecursionlimit


# Ограничение количество рекурсий
setrecursionlimit(1_000)


# Функция генерация сделки
def generate_trade(inventory: dict) -> dict:
    # Конструкция try/except для обработки, когда у пользователя мало предметов
    try:
        # получения случайного курса (материал1 к материалу2) и цены
        ((need, sell), price) = choice(list(COURSES.items()))
        # Получения максимального значения материала1 на продажу
        max_need_count = inventory.get(need, 0)
        # Если недостаточно материала1 (цена больше)
        if max_need_count < price:
            # То начать функцию заново
            return generate_trade(inventory)
        # Определяем случайное количество покупаемого товара
        sell_count = randint(1, max_need_count // price)
        # Возращение словаря
        return {
            "text": f"Даешь:\n{ITEMS[need]['name']} {sell_count * price}\nПолучаешь:\n{ITEMS[sell]['name']} {sell_count}",
            "need_material": need,
            "sell_material": sell,
            "need_count": sell_count * price,
            "sell_count": sell_count,
            "is_right": True
        }
    except RecursionError:
        # Возращение словаря с ошибкой
        return {
            "text": "У тебя недостаточно предметов для обмена",
            "need_material": 0,
            "sell_material": 0,
            "need_count": 0,
            "sell_count": 0,
            "is_right": False
        }
