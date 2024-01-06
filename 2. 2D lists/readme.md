## Домашнее задание Двумерные списки №2
  ### Задание
  1. Создайте двумерный массив размером 3 на 3.
  2. Заполните его числами от 1 до 9. (используйте генератор)
  3. Затем программа должна выводить строку из элементов каждой строки массива.


## Примеры ввода/вывода 
  | Ввод  | Вывод  |
  |:-:|:---------------:|
  | *отсутствует* | 1 2 3 4 5 6 7 8 9  |

## Алгоритм решения
  1. Создаем двумерный массив (или же матрицу) используя генератор <br>
    `for i in range(N)` - генерация строк, где **`N`** - кол-во строк в матрице <br>
    `for j in range(M)` - генерация колонок, где **`M`** - кол-во колонок в матрице <br>
    `j + i * N + 1` - формула заполнения ячеек в матрице, где **`j`** - индекс колонки, **`i`** - индекс строки, **`N`** - кол-во строк в матрице <br>
    Из условия наши **`N`** и **`M`** равны 3 (`Создайте двумерный массив размером `**`3`**` на `**`3`**`.`)
  ```py
  matrix = [[j + i * 3 + 1 for j in range(3)] for i in range(3)]
  ```
  2. Используем цикл `for` для перебора строк в матрице и выводим массив (строку), используя специальный оператор `*`
     Он работает примерно так
     ```py
     data = (1, 2, 3, 4)
     print(data[0], data[1], data[2], data[3], sep='', end='!\n')
     print(*data, sep='*', end='?')
     ```
     Вывод будет таким:
     ```
     1234!
     1*2*3*4?
     ```
     Необязательные ргументы `sep` и `end` это разделитель и конец строки, по умолчанию у них значение ' ' (пробел) и '\n' (знак новая строка)
     С помощью такого оператора можно выводить все элементы массива легче.
  ```py
  for line in matrix:
    print(*line, end=" ")
  ```

## Полный код, без комментариев
```py
matrix = [[j + i * 3 + 1 for j in range(3)] for i in range(3)]
for line in matrix:
    print(*line, end=" ")
```
<p align="center">
    <a href="../1. repeat_sorting/readme.md">
      <img alt="Предыдущее задание" src="https://img.shields.io/badge/%D0%9F%D1%80%D0%B5%D0%B4%D1%8B%D0%B4%D1%83%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="../3. classes&object/readme.md">
      <img alt="Следующее задание" src="https://img.shields.io/badge/%D0%A1%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B5%D0%B5-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-e22445?style=for-the-badge&logo=accenture&logoColor=e22445">
    </a>
</p>
