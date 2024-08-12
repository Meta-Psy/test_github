menu = input('Выберите действие: \n\n'
             '1 - Добавить продукт\n'
             '2 - Посмотреть склад\n')
sklad = {}
if menu == 1:
    product = input('Введите название продукта: ')
    if product in sklad:
        print('Продукт уже есть на складе')
    else:
        numbers = float(input('Введите количество продукта: '))
        sklad[product] = numbers
        print(sklad)