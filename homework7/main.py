from copy import deepcopy

users = [
    {
        "name": "Paul",
        "age": 17,
        "favorites": {
            "colors": ['red', 'orange'],
            "food": ['burger', 'pizza']
        }
    },
    {
        "name": "Jane",
        "age": 21,
        "favorites": {
            "colors": ['purple'],
            "food": ['salad', 'ice scream', 'fish']
        }
    },
    {
        "name": "James",
        "age": 26,
        "favorites": {
            "colors": ['pink', 'white', 'black'],
            "food": ['chips', 'coca cola']
        }
    }
]

users_copy = deepcopy(users)
users_copy[1]["age"] = 20
users_copy[-1]["favorites"]["food"].append("banana")
print(*users, '\n', *users_copy, sep='\n')