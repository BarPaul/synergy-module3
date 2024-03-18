# Импортирование нужных модулей/пакетов
from items import ITEMS
from config import HUNT_MESSAGES
from random import choices, randint, choice


# Функция генерирования награды за охоту
def generate_reward() -> dict | None:
    # Генерирование списка награды с количеством материалов от 0 до 5
    items = [_generate_item() for _ in range(randint(0, 5))]
    # Если список имеет награды, то
    # Вернуть превращение в словарь с ключем "материал" и значением количество-повторения в списке
    # Если нет, то вернуть None
    return {word: items.count(word) for word in items} if items else None


# Функция генерации сообщения на охоту
def generate_message() -> dict:
    # Возращение случайного сообщения
    return choice(HUNT_MESSAGES)


# Функция генерации одного предмета
def _generate_item() -> str:
    # Берем проценты, название предметов и с учетом этого выбираем случайное значение и превращаем список в строку
    return ''.join(choices(list(ITEMS.keys()), weights=[item['percent'] * 100 for item in ITEMS.values()]))


# Функция конвентирования словаря инвентарь в строку
def convert_inventory(inventory: dict) -> str:
    # По шаблону Название материала количество
    return '\n'.join([f'{ITEMS[k]["name"]} {v}' for k, v in inventory.items()])
