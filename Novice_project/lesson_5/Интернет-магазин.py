all_products = {}
korzinka = {}

while True:
    menu = int(input('Кем вы являетесь?: \n\n'
            '1 - Покупатель\n' 
            '2 - Владелец магазина\n'
            '3 - Выход\n'))
    if menu == 1:
        customer_menu = int(input('Выберите действие: \n\n'
                                  '1 - Просмотреть корзину\n'
                                  '2 - Просмотреть товары\n'
                                  '3 - Добавить товар в корзину\n'
                                  '4 - Удалить товар из корзины\n'
                                  '5 - Вернуться в начальное меню\n'
                                  '6 - Выход\n'))
        if customer_menu == 1:
            count = 0
            for k, v in korzinka.items():
                count += 1
                print(f'Ваша корзина: {k} : {v} кг/шт')
        elif customer_menu == 2:
            count = 0
            for k, v in all_products.items():
                count += 1
                print(f'{count}. {k} : {v} кг/шт')
        elif customer_menu == 3:
            count = 0
            for k, v in all_products.items():
                count += 1
                print(f'{count}. {k} : {v} кг/шт')
            product_add = str(input('Выберите из перечисленных товаров нужный: ')).lower()
            if product_add in all_products:
                numbers = float(input('В каком количестве желаете приобрести?'))
                x = float(all_products.get(product_add)) - numbers
                if x <= 0:
                    print(f'К сожалению, на данный момент у нас в наличии только {all_products.get(product_add)} шт/кг ')
                else:
                    korzinka[product_add] = numbers
                    all_products[product_add] = x
                    print(f'{product_add} добавлен в корзину')
            else: print('Такого продукта нет на складе.')
        elif customer_menu == 4:
            count = 0
            for k, v in korzinka.items():
                count += 1
                print(f'{k} : {v} кг/шт')
            menu_korzina = int(input('Выберите действие\n\n'
                                     '1 - Удалить все и завершить операцию\n'
                                     '2 - Удалить продукт из списка\n'
                                     '3 - Уменьшить количество одного из продуктов\n'))
            if menu_korzina == 1:
                korzinka.clear()
                print('Ваши продукты успешно удалены')
                count = 0
                for k, v in korzinka.items():
                    count += 1
                    print(f'{k} : {v} кг/шт')
            elif menu_korzina == 2:
                count = 0
                for k, v in korzinka.items():
                    count += 1
                    print(f'{k} : {v} кг/шт')
                product_del = input('Введите имя продукта, который вы хотели бы удалить: ').lower()
                if product_del in korzinka:
                    korzinka.pop(product_del)
                    print(f'{product_del} успешно удален(а) из корзины')
                else:
                    print('Такого продукта нет в корзине')
            elif menu_korzina == 3:
                count = 0
                for k, v in korzinka.items():
                    count += 1
                    print(f'{k} : {v} кг/шт')
                product_del = input('Введите имя продукта, который вы хотели бы удалить: ').lower()
                if product_del in korzinka.keys():
                    product_del_number = int(input(f'В каком количестве, хотели бы удалить {product_del}?'))
                    x = korzinka.get(product_del) - product_del_number
                    if x >= 0:
                        korzinka[product_del] = x
                        print(f'{product_del} удален')
                        all_products[product_del] = all_products[product_del] + product_del_number
                    else:
                        print('В вашей корзине нет столько товаров')
                else:
                    print(f'{product_del} нет в корзине')
            else:
                print('Такой функции не существует')
                product_add = str(input('Выберите из перечисленных товаров нужный: ')).lower()
                numbers = float(input('В каком количестве желаете приобрести?'))
        elif customer_menu == 5:
            break
        elif customer_menu == 6:
            break
        else:
            print('Такой функции не существует, попробуйте еще раз')
    elif menu == 2:
        menu_owner = int(input('Выберите действие\n\n'
                                 '1 - Добавить продукт на склад\n'
                                 '2 - Удалить продукт со склада\n'
                                 '3 - Посмотреть, что есть на складе\n'))
        if menu_owner == 1:
            name = input("Введите название продукта: ").lower()
            amount = float(input("Введите количество: "))
            all_products[name] = int(amount)
            print("Продукт добавлен")
        elif menu_owner == 2:
            count = 0
            for k, v in all_products.items():
                count += 1
                print(f'{count}. {k} : {v} кг/шт')
            product_del_owner = input('Введите имя товара, который хотели бы удалить: ').lower()
            if product_del_owner in all_products:
                all_products.pop(product_del_owner)
                print(f'Товар {product_del_owner} успешно удален.')
            else:
                print(f'Товара {product_del_owner} на складе не существует')
        elif menu_owner == 3:
            count = 0
            for k, v in all_products.items():
                count += 1
                print(f'{count}. {k} : {v} кг/шт')
    elif menu == 3:
        break
    else:
        print('Такой функции не существует, попробуйте еще раз')
