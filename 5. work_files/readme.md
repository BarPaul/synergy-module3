## Домашнее задание Работа с Файлами №5
  ### Задание
  1. Создайте текстовый файл с названием "`sample.txt`"
  2. Напишите программу для чтения и вывода его содержимого на экран.


## Примеры ввода/вывода 
  | sample.txt  | Вывод  |
  |:-----------:|:------:|
  | Hello, World | Hello, World |
  | It's first line <br>It's second line | It's first line <br>It's second line |
  | *пустой*  | *пустая строка* |

## Алгоритм решения
  1. С помощью функции `open()` и контекстного менеджера `with` открываем файл <br>
    1.1 Сохраняем файл в переменную f <br>
    1.2 С помощью метода `read()` получаем текст файла `sample.txt` и выводим этот текст
  ```py
  with open("sample.txt") as f:
      print(f.read())
  ```
  <details>
    <summary>Открой если непонятно</summary>
  
### Теория
   Функция `open()` принимает 2 аргумента название файла или путь к нему и режим открытия, по умолчанию '`r`' <br>
  '`r`' - режим чтения, <br>
  '`w`' - режим записи, при которой удаляется весь прошлый текст файла и добавляется новый  <br>
  '`a`' - режим дозаписи <br>
  Есть многие остальные, но эти три основных режима <br>
  Контекстный менеджер это конструкция <br>
  ```py
  with function() as variable
  ```
  С помощью него мы можем безопасно открыть файл, к примеру когда в ходе записи в файл появляется ошибка, то с этим кодом файл останется открытым (функция `f.close()` не исполнится) и будет занимать место в памяти
  ```py
  f = open("sample.txt", "w")
  f.write("что-то, что возможно вызовет ошибку")
  f.close()
  ```
  А такой код выглядит не только лучше, но еще закроет файл в любом случае после исполнения кода
  ```py
  with open("sample.txt", "w") as f:
    f.write("что-то, что возможно вызовет ошибку")
  ```
  </details>

## Полный код, без комментариев
```py
with open("sample.txt") as f:
      print(f.read())
```

<p align="center">
    <a href="../4. inheritance/readme.md">
      <img alt="Предыдущее задание" src="https://img.shields.io/badge/%D0%9F%D1%80%D0%B5%D0%B4%D1%8B%D0%B4%D1%83%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="../6. pygame_project/readme.md">
      <img alt="Следующее задание" src="https://img.shields.io/badge/%D0%A1%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
</p>
