# Список предметов
ITEMS = {
    # Заполнение по шаблону
    # 'айди': {
    #       'name': 'отображаемое имя',
    #       'percent': количество процентов десятичной дробью
    # }
    'meat': {
        'name': '🍖 мясо',
        'percent': 0.20
    },
    'water': {
        'name': '💧 вода',
        'percent': 0.50
    },
    'copper': {
        'name': '🥉 медь',
        'percent': 0.10
    },
    'iron': {
        'name': '🥈 железо',
        'percent': 0.07
    },
    'glass': {
        'name': '🪟 стекло',
        'percent': 0.10
    },
    'gold': {
        'name': '🪙 монета',
        'percent': 0.03
    }
}


# Курсы "материал1 к материал2", к примеру нужно 5 водичек, чтоб получить одно мясо
COURSES = {
    ('water', 'meat'): 5,
    ('meat', 'copper'): 10,
    ('meat', 'iron'): 15,
    ('meat', 'glass'): 10,
    ('meat', 'gold'): 20,
    ('copper', 'gold'): 2,
    ('iron', 'gold'): 2
}
