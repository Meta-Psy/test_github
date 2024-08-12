class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Нельзя делить на нуль"

    def subtraction(self):
        return self.a - self.b

while True:
    problem1 = Math(a=float(input('Введите первое число: ')), b=float(input('Введите второе число: ')))
    menu = int(input('Выберите действие: \n\n'
                     '1 - Сложить\n'
                     '2 - Отнять\n'
                     '3 - Умножить\n'
                     '4 - Поделить\n'
                     '5 - Выйти\n'))
    if menu == 1:
        print('Результат: ', problem1.addition())
    elif menu == 2:
        print('Результат: ', problem1.subtraction())
    elif menu == 3:
        print('Результат: ', problem1.multiplication())
    elif menu == 4:
        print('Результат: ', problem1.division())
    elif menu == 5:
        print('Выход из программы.')
        break
    else:
        print('Такой функции не существует.')