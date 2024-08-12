# Меню пользователя
contacts = ['Алексей']
numbers = ['933977109']
cont_numb = ['Алексей', '933977109']
menu = int(input('Выберите необходимое действие: 1 - добавить контакт, 2 - удалить контакт, 3 - изменить контакт: '))

# Функция добаления контактов
if menu == 1:
    new_contact = str(input('Введите имя нового контакта: '))
    new_number = str(input('Введите номер контакта: '))
    if new_contact in contacts and new_number not in numbers:
        old_contact = contacts.index(new_contact)
        old_number = numbers[old_contact]
        print(f'Такой контакт уже существует. {new_contact} - {old_number}. Все равно хотите добавить? 1 - Да, 2 - Нет')
        choice1 = int(input('Введите ваш выбор в виде числа: '))
        if choice1 == 1:
            contacts.append(new_contact)
            numbers.append(new_number)
            cont_numb.extend([new_contact, new_number])
            print(f'Контакт {new_contact} - {new_number} добавлен')
            print(f'{cont_numb}')
        elif choice1 == 2:
            print('Для следующей операции, начните запрос заново')
    elif new_number in numbers and new_contact not in contacts:
        old_number = numbers.index(new_number)
        old_contact = contacts[old_number]
        print(f'Такой номер уже существует. {old_contact} - {new_number}. Все равно хотите добавить? 1 - Да, 2 - Нет')
        choice2 = int(input('Введите ваш выбор в виде числа: '))
        if choice2 == 1:
            contacts.append(new_contact)
            numbers.append(new_number)
            cont_numb.extend([new_contact, new_number])
            print(f'Контакт {new_contact} - {new_number} добавлен')
            print(f'{cont_numb}')
        elif choice2 == 2:
            print('Для следующей операции, начните запрос заново')
            print(f'{cont_numb}')
    elif new_contact in contacts and new_number in numbers:
        print('Такой контакт уже существует')
        print('Для следующей операции, начните запрос заново')
    else:
        contacts.append(new_contact)
        numbers.append(new_number)
        cont_numb.extend([new_contact, new_number])
        print(f'Контакт {new_contact} - {new_number} добавлен')
        print(f'{cont_numb}')

# Функция удаления контактов
if menu == 2:
    print(f'{cont_numb}')
    choice3 = int(input('Выберите 1 - удалить один контакт, или 2 - удалить все контакты: '))
    if choice3 == 1:
        del_contact = str(input('Введите имя контакта, которого хотите удалить: '))
        if del_contact not in contacts:
            print('Такого имени не существует')
        else:
            del_number = str(input('Введите номер контакта, которого хотите удалить: '))
            if del_number not in numbers:
                print('Такого номера не существует')
            elif del_contact in contacts and del_number in numbers:
                index_contact_del = contacts.index(del_contact)
                index_number_del = numbers.index(del_number)
                contacts.pop(index_contact_del)
                numbers.pop(index_number_del)
                cont_numb.remove(del_contact)
                cont_numb.remove(del_number)
                print(f'{cont_numb}')
    elif choice3 == 2:
        contacts.clear()
        numbers.clear()
        cont_numb.clear()
        print(f'{cont_numb}')

# Функция изменения контактов
if menu == 3:
    izm_contact = str(input('введите имя контакта, которого хотели бы заменить:  '))
    if izm_contact not in contacts:
        print('Такого имени не сущетсвует')
    elif izm_contact in contacts:
        izm_number = str(input('Введите номер контакта, которого хотели бы заменить: '))
        if izm_number in numbers:
            newest_contact = str(input('Введите имя, на которое вы хотели бы заменить предыдущее: '))
            newest_number = str(input('Введите номер, на который вы хотите заменить предыдущий: '))
            index_contact_izm = contacts.index(izm_contact)
            index_number_izm = numbers.index(izm_number)
            contacts[index_contact_izm] = newest_contact
            numbers[index_number_izm] = newest_number
            a = cont_numb.index(izm_contact)
            b = cont_numb.index(izm_number)
            cont_numb[a] = newest_contact
            cont_numb[b] = newest_number
            print('Заменено')
            print(f'{cont_numb}')
        elif izm_number not in numbers:
            print('Такого номера не существует')
