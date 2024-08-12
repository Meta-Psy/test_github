all_products = {}
while True:
    menu = input("Выберите действие:\n"
                 "1 - Добавить товар на склад: \n"
                 "2 - Посмотреть продукты: \n")
    if menu == "1":
        name = input("Введите название продукта: ")
        amount = input("Введите количество: ")
        all_products[name] = int(amount)
        print("Продукт добавлен")
    elif menu == "2":
        count = 0
        for k, v in all_products.items():
            count += 1
            print(f"{count}. {k} : {v} кг")
