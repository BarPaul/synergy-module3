# Импортирование нужного модуля
from sqlite3 import connect


# Создание класса Database
class Database:

    # Метод конструктор
    def __init__(self):
        # Создаем файл database.db
        self.conn = connect('database.db', check_same_thread=False)
        self.cur = self.conn.cursor()
        # Выполняем первый запрос "СОЗДАТЬ ТАБЛИЦУ ЕСЛИ НЕ СУЩЕСТВУЕТ пользователи с полями айди числового типа и инвентарь текстового типа"
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER,
            inventory TEXT
            )''')

    # Метод на проверку есть пользователь в таблице или нет
    def is_new(self, id: int) -> bool:
        # Исполнение запроса "ВЫБРАТЬ айли ИЗ пользователей ГДЕ айди = {id}"
        self.cur.execute("SELECT id FROM users WHERE id = ?", (id,))
        # Если пользователь не найден, то self.cur.fetchone() is None
        # Иначе, будет False
        return self.cur.fetchone() is None

    # Метод добавления пользователя в таблицу
    def insert_user(self, id: int):
        # Исполнение запроса "ВСТАВИТЬ В пользователей ЗНАЧЕНИЯ ({id}, "")"
        self.cur.execute("INSERT INTO users VALUES(?, ?)", (id, ""))
        # Применить изменения
        self.conn.commit()
    
    # Метод удаления пользователя из таблицы
    def delete_user(self, id: int):
        # Выполнение запроса "УДАЛИТЬ ИЗ пользователь ГДЕ айди = {id}"
        self.cur.execute("DELETE FROM users WHERE id = ?", (id,))
        # Применить изменения
        self.conn.commit()
    
    # Метод получения инвентаря пользователя
    def get_inventory(self, id: int) -> dict | None:
        # Обработка ошибок try/except
        try:
            # Выполнение запроса "ВЫБРАТЬ инвентарь ИЗ пользователей ГДЕ айди = {id}"
            self.cur.execute("SELECT inventory FROM users WHERE id = ?", (id,))
            # Вернуть преобразованную строку в словарь (для деления материалов, количества используется "-", а для деления материала от количества " ")
            return {item.split()[0]: int(item.split()[-1]) for item in self.cur.fetchone()[0].split("-")}
        except IndexError:
            # Если инвентарь пуст
            return None

    # Метод обновления инвентаря (инкапсулирован)
    def _update_inventory(self, id: int, inventory: dict):
        # Выполнить "ОБНОВИТЬ пользователей ПОСТАВИТЬ ЗНАЧЕНИЕ инвентарь = {convert_inventory(inv)} ГДЕ айди = {id}"
        self.cur.execute("UPDATE users SET inventory = ? WHERE id = ?", (self._convert_inventory(inventory), id,))
        # Применить изменения
        self.conn.commit()
    
    # Метод конвертации инвентаря (инкапсулирован)
    def _convert_inventory(self, inventory: dict) -> str:
        # Конвертация инвентаря из словаря в строку
        return '-'.join([' '.join([k, str(v)]) for k, v in inventory.items()])
    
    # Метод добавления предмета в инвентарь
    def add_item(self, id: int, item: str, count: int = 1):
        # Получения инвентаря
        inventory = self.get_inventory(id)
        # Если инвентарь пуст
        if inventory is None:
            # Инвентарь равен {материал: количество}
            inventory = {item: count}
        # Иначе если материал в материалах инвентаря
        elif item in inventory.keys():
            # Прибавить к ключевому значению количество материала
            inventory[item] += count
        # Иначе
        else:
            # Ключевое значение материала равна количеству
            inventory[item] = count
        # Обновление инвентаря
        self._update_inventory(id, inventory)
    
    # Метод "сбора", "удаления" предмета из инвентаря
    def rem_item(self, id: int, item: str, count: int = 1):
        # Получения инвентаря
        inventory = self.get_inventory(id)
        # Если материал есть в материалах инвентаря
        if item in inventory.keys():
            # Отнять у ключевого значения количество материала
            inventory[item] -= count
        # Если материала меньше или равно 0
        if inventory[item] <= 0:
            # Удаление окончательно из инвентаря
            inventory.pop(item)
        # Обновление инвентаря
        self._update_inventory(id, inventory)
