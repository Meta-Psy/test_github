class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, add):
        self.balance += add
        print(f'Баланс успешно пополнен на {add} $. Ваш баланс сейчас {self.balance} $')
    def cash(self, minus):
        if self.balance - minus < 0:
            print('Не достаточно денег на счете')
        else:
            self.balance = self.balance - minus
            print(f'Успешно снято: {minus} $. Ваш баланс сейчас: {self.balance} $')
    def my_balance(self):
        print(f'Ваш баланс {self.balance} $')
    def __repr__(self):
        return f'Этот объект относится к классу BankAccount c атрибутами {vars(self)}'

while True:
    client1 = BankAccount('Alex', 10000)
    menu = str(input('Выберите действие:\n\n'
                     '1 - Пополнить счёт: \n'
                     '2 - Снять деньги: \n'
                     '3 - Ваш баланс: \n'))
    if menu == '1':
        client1.deposit(add=float(input('Внесите депозит')))
    elif menu == '2':
        client1.cash(minus=float(input('Укажите сумму, которую хотели бы снять')))
    elif menu == '3':
        client1.my_balance()
