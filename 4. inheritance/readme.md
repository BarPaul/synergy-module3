## Домашнее задание Наследование в классах, создание собственных объектов №4
  ### Задание
  1. Создайте родительский класс `Animal` с атрибутами `name` и `species`. <br>
    1.1 Дайте ему метод `make_sound()`, который выводит звук, издаваемый животными.
  2. Создайте дочерние классы (подклассы) `Dog` и `Cat`, которые наследуют от класса `Animal`. <br>
    2.1 Дайте каждому из них свой собственный метод `make_sound()`, который выводит соответствующий звук ("`Гав`" для собаки и "`Мяу`" для кота).


## Примеры ввода/вывода 
  | Ввод  | Вывод  |
  |:-:|:---------------:|
  | *отсутствует* | _<Имя>_ _<Порода>_ говорит Гав |
  | *отсутствует* | _<Имя>_ _<Порода>_ говорит Мяу |
  | *отсутствует* | Животное _<Имя>_ _<Порода>_ не имеет своего звука |

## Алгоритм решения
  1. Создаем класс `Animal` <br>
    1.1 Добавляем метод-конструктор `__init__`, который принимает 2 аргумента `name` и `species` <br>
    1.2 Определяем аттрибуты класса с помощью данных из этих аргументов
  ```py
  class Animal:
      def __init__(self, name, species):
          self.name = name
          self.species = species
  ```
  2. Добавляем метод `make_sound()` <br>
    2.1 Делаем вывод, что "Животное _<Имя>_ _<Порода>_ не имеет своего звука" (в целом можно любой другой текст)
  ```py
  class Animal:
      # Часть прошлого кода...
      def make_sound(self):
          print(f"Животное {self.name} {self.species} не имеет своего звука")
  ```
  3. Создаем класс `Dog` с родительским классом Animal <br>
    3.1 Переопределяем (пересоздаем) метод `make_sound()`
  ```py
  # Прошлый код...
  class Dog(Animal):
      def make_sound(self):
          print(f"{self.name} {self.species} говорит Гав")
  ```
  4. По аналогии с классом `Dog` создаем класс `Cat`
  ```py
  # Прошлый код...
  class Cat(Animal):
      def make_sound(self):
          print(f"{self.name} {self.species} говорит  Мяу")
  ```
  <details>
      <summary>Открой, если непонятно</summary>
    Наследование работает, так: <br>
    Есть родительский и дочерний класс. Родительским называется, если от него наследуется другой класс, который будет называться дочерним. <br>
    При наследовании дочерний класс получает все методы и аттрибуты из родительского, но так же в дочернем можно переопределить (создать свой) метод родительского класса. <br>
  </details>

## Полный код, без комментариев
```py
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"Животное {self.name} {self.species} не имеет своего звука")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} {self.species} говорит Гав")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} {self.species} говорит Мяу")
```

<p align="center">
    <a href="../3. classes&object/readme.md">
      <img alt="Предыдущее задание" src="https://img.shields.io/badge/%D0%9F%D1%80%D0%B5%D0%B4%D1%8B%D0%B4%D1%83%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="../5. work_files/readme.md">
      <img alt="Следующее задание" src="https://img.shields.io/badge/%D0%A1%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
</p>
