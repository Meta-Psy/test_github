class Car:
    def __init__(self, color, car_type, year='Нет данных'):
        self.color = color
        self.car_type = car_type
        self.year = year

    def turn_on(self):
        print('Автомобиль заведен')

    def turn_off(self):
        print('Автомобиль заглушен')

    def set_year(self):
        self.year = input('Введите год выпуска автомобиля: ')
        print(f'Год выпуска заменен на {self.year}')

    def set_type(self):
        self.car_type = input('Введите тип автомобиля: ')
        print(f'Тип автомобиля заменен на {self.car_type}')

    def set_color(self):
        self.color = input('Укажите цвет машины: ')
        print(f'Цвет автомобиля заменен на {self.color}')

    def info(self):
        print(f"Цвет: {self.color}, Тип: {self.car_type}, Год: {self.year}")

car = Car(color="Красный", car_type="Седан")

while True:
    menu = int(input('Выберите действие: \n\n'
                     '1 - Завести автомобиль\n'
                     '2 - Заглушить автомобиль\n'
                     '3 - Изменить год выпуска\n'
                     '4 - Изменить тип автомобиля\n'
                     '5 - Изменить цвет автомобиля\n'
                     '6 - Показать информацию об автомобиле\n'
                     '7 - Выйти\n'))

    if menu == 1:
        car.turn_on()
    elif menu == 2:
        car.turn_off()
    elif menu == 3:
        car.set_year()
    elif menu == 4:
        car.set_type()
    elif menu == 5:
        car.set_color()
    elif menu == 6:
        car.info()
    elif menu == 7:
        print('Выход из программы.')
        break
    else:
        print('Такой функции не существует.')