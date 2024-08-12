
def add(name, number):
    if name in dict.keys():
        return print('Такой клиент уже существует')
    else:
        dict[name] = number
        return print(f'Клиент {name} был добавлен')
def delite(name):
    if name in dict.keys():
        dict.pop(name)
        return print(f'Клиент {name} был удален')
    else:
        return print(f'Клиент {name} не в списке')
def see(dict):
    print(f'Список клиентов: {dict}')
dict = {}
while True:
    menu = int(input('Какое действие вам необходимо выполнить? \n\n'
                     '1 - Добавить клиента\n'
                     '2 - Удалить клиента\n'
                     '3 - Просмотреть занятые номера\n'
                     '4 - Завершить операцию'))

    if menu == 1:
        name = str(input('Введите имя клиента: '))
        number = int(input('Введите номер клиента: '))
        add(name, number)
    elif menu == 2:
        name = str(input('Введите имя клиента, которого хотите удалить'))
        delite(name)
    elif menu == 3:
        see(dict)
