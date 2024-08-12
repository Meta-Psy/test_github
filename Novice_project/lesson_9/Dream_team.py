class Players:
    def __init__(self, name, number, value=False):
        self.name = name
        self.number = number
        self.value = value

    def run(self, value=False):
        if value == False:
            self.value = True
        else:
            self.value = False

    def pas(self, value=False):
        if value == False:
            self.value = True
        else:
            self.value = False

class Napadayushiy(Players):
    def __init__(self, name, number, attack1=False):
        super().__init__(name, number)
        self.attack1 = attack1

    def attack(self, attack1=False):
        if attack1 == False:
            self.attack1 = True
            print('В атаке')
        else:
            self.attack1 = False
            print('Не в атаке')

class Zashitnik(Players):
    def __init__(self, name, number, defense1=False):
        super().__init__(name, number)
        self.defense1 = defense1

    def defense(self, defense1=False):
        if defense1 == False:
            self.defense1 = True
            print('В защите')
        else:
            self.defense1 = False
            print('Вышел из защиты')
class SemiZashitnik(Napadayushiy, Zashitnik):
    def __init__(self, name, number, max_meters=0):
        Napadayushiy.__init__(self, name, number)
        Zashitnik.__init__(self, name, number)
        self.max_meters = max_meters

    def long_pass(self, max_meters=0):
        self.max_meters = max_meters
        print(f'Показатель длинного паса: {self.max_meters}')

class Goalkeeper(Players):
    def __init__(self, name, number, numbers=0):
        super().__init__(name, number)
        self.numbers = numbers

    def max_goalkeeping(self, numbers=0):
        self.numbers = numbers
        print(f'Количество всех голов: {self.number}')

player1 = Napadayushiy('Alex', '1')
player2 = Zashitnik('Botir', '2')
player3 = SemiZashitnik('Sardor', '3')

a = player3.attack(False)
print(a)
