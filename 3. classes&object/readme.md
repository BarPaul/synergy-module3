## Домашнее задание Введение в ООП. Классы и объекты №3
  ### Задание
  1. Создайте класс `Car`, который имеет атрибуты `mark` (марка автомобиля), `model` (модель автомобиля) и `year` (год выпуска).
  2. Дайте ему метод `display_info()`, который выводит информацию о машине (марка, модель и год).


## Примеры ввода/вывода 
  | Ввод  | Вывод  |
  |:-:|:---------------:|
  | *отсутствует* | Марка: Лада<br>Модель: Веста<br>Год выпуска: 2023 |
  | *отсутствует* | Марка: Тесла<br>Модель: С<br>Год выпуска: 2022 |
  | *отсутствует* | Марка: Киа<br>Модель: Рио<br>Год выпуска: 2021 |

## Алгоритм решения
  Как и в первой задачи данные машины у нас произвольные <br>
  1. Создаем класс `Car` с помощью ключевого слова `class`. <br>
  1.1 К классу `Car` добавляем метод-конструктор `__init__`, в котором нужны аргументы марка, модель и год выпуска. <br>
  1.2 Присваем аттрибуты `mark`, `model`, `year` данными из аргументов <br>
  ```py
  class Car:
    def __init__(self, mark, model. year):
      self.mark = mark
      self.model = model
      self.year = year
  ```
  2. Добавляем к классу метод `display_info()` <br>
    2.1 Делаем выводы для каждого значение о класса с помощью F-строк
  ```py
  class Car:
    # Часть прошлого кода ...
    def display_info():
      print(f"Марка: {self.mark}")
      print(f"Модель: {self.model}")
      print(f"Год выпуска: {self.year}")
  ```
## Полный код, без комментариев
```py
class Car:
    def __init__(self, mark, model. year):
      self.mark = mark
      self.model = model
      self.year = year

    def display_info():
      print(f"Марка: {self.mark}")
      print(f"Модель: {self.model}")
      print(f"Год выпуска: {self.year}")
```

<p align="center">
    <a href="../2. 2D lists/readme.md">
      <img alt="Предыдущее задание" src="https://img.shields.io/badge/%D0%9F%D1%80%D0%B5%D0%B4%D1%8B%D0%B4%D1%83%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="../4. inheritance/readme.md">
      <img alt="Следующее задание" src="https://img.shields.io/badge/%D0%A1%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
</p>
