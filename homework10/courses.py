# Импортирование нужных библиотек
from requests import get, exceptions
from dataclasses import dataclass
from random import choice
from flag import flagize
from config import URL


# Создание датакласса курсы
@dataclass
class Course:
    Name: str
    CharCode: str
    Value: float
    
    # Магический метод str(Course)
    def __str__(self) -> str:
        return flagize(f':{self.CharCode[:2]}: Курс *{self.CharCode}* к *RUB*:\n1 {self.Name} = {self.Value:.2f} руб.')
    
    # Магический метод __hash__
    def __hash__(self) -> int:
        # Магический метод __hash__ у str(Course)
        return self.__str__().__hash__()


# Получение нескольких курсов
def get_courses(n: int) -> list[Course | str]:
    # Использование функции _get_course N раз
    # Пока длина курсов без повторений не равна N
    while len(set(data := [_get_course() for _ in range(n)])) != n:
        # перегенировать курсы
        data = [_get_course() for _ in range(n)]
    # Вернуть курсы
    return data


# Получение одного курса (инкапсулирован)
def _get_course() -> Course | str:
    # Обработка ошибок try/except (если запрос отправлен неудачно)
    try:
        # Получение словаря валют
        data = get(URL).json()['Valute']
        # Получение случайного курса валюты
        (_, course) = choice(list(data.items()))
        # Возращение класса
        return Course(course['Name'], course['CharCode'], course['Value'])
    except (exceptions.JSONDecodeError, KeyError):
        # Непридвиденная ошибка
        return "Непридвиденная ошибка!"
