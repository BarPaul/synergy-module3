class Car:

    def __init__(self, make="Mercedes", model="Benz", year=2023):
        self.mark = make
        self.model = model
        self.year = year
        self.about = {
            "Марка": self.mark,
            "Модель": self.model,
            "Год выпуска": self.year
        }

    def display_info(self) -> str:
        info_text = ''
        for key, value in self.about.items():
            info_text += f"{key}: {value}\n"
        print(info_text[:-2])
        return info_text[:-2]
    
    def __str__(self) -> str:
        print_massive = [f"{k}: {v}" for k, v in self.about.items()]
        return '\n'.join(print_massive)

def main() -> tuple:
    car1 = Car()
    car2 = Car("Lada", "Niva", 2021)
    for car in [car1, car2]:
        car.display_info()
        print(car)
    return car1, car2

if __name__ == '__main__':
    main()
