class Animal:
    def __init__(self, name="человек", species="разумный") -> None:
        self.name = name
        self.species = species
    
    def make_sound(self) -> str:
        sad_message = f"У организма {self.name} {self.species} нет звука :("
        print(sad_message)
        return sad_message


class Dog(Animal):
    def make_sound(self) -> str:
        dog_message = f"Гав-гав (звуки исходят из собаки {self.name} {self.species})"
        print(dog_message)
        return dog_message


class Cat(Animal):
    def make_sound(self) -> str:
        cat_message = f"Мяу (звуки исходят из кота {self.name} {self.species})"
        print(cat_message)
        return cat_message


def main() -> tuple:
    dog = Dog("Овчарка", "Немецкая")
    cat = Cat("Мейн-кун", "Серебристый")
    unknown = Animal("Бабайка", "Страшная")
    dog_sound = dog.make_sound()
    cat_sound = cat.make_sound()
    unknown_sound = unknown.make_sound()
    return dog_sound, cat_sound, unknown_sound


if __name__ == '__main__':
    main()
