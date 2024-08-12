def search(name):
    name = name.lower()
    for class_key, dict_alphabet in classes.items():
        for alphabet, dict_pupils in dict_alphabet.items():
            for pupil_name in dict_pupils:
                if name == pupil_name.lower():
                    return class_key, alphabet, pupil_name
    return None

def add():
    new_class = str(input('Введите класс, в котором обучается ученик: 1, 2, 3, 4 '))
    alphabet_class = str(input('Введите букву класса: (A, B, C, D, E, F)')).upper()
    new_name = str(input('Введите Ф.И.О. ученика, которого хотите добавить: '))
    new_number = str(input('Введите номер телефона этого ученика: '))

    search_result = search(new_name)
    if search_result:
        print('Ученик с таким именем или номером уже существует в списке')
        print(classes)
        menu_add = str(input('Выберете дальнейшее действие: \n\n'
                             '1 - Все равно добавить и сохранить найденного ученика.\n'
                             '2 - Заменить ученика.\n'
                             '3 - Ничего не изменять\n'))
        if menu_add == '1':
            if new_class not in classes:
                classes[new_class] = {}
            if alphabet_class not in classes[new_class]:
                classes[new_class][alphabet_class] = {}
            classes[new_class][alphabet_class][new_name] = new_number
            print(f'Ученик {new_name} добавлен')
            print(classes)
        elif menu_add == '2':
            class_key, alphabet, pupil_name = search_result
            classes[class_key][alphabet].pop(pupil_name)
            if new_class not in classes:
                classes[new_class] = {}
            if alphabet_class not in classes[new_class]:
                classes[new_class][alphabet_class] = {}
            classes[new_class][alphabet_class][new_name] = new_number
            print(f'Ученик {new_name} удален и заменен на новое имя и номер телефона')
        elif menu_add == '3':
            print('Ничего не изменено')
            print(classes)
    else:
        if new_class not in classes:
            classes[new_class] = {}
        if alphabet_class not in classes[new_class]:
            classes[new_class][alphabet_class] = {}
        classes[new_class][alphabet_class][new_name] = new_number
        print(f'Ученик {new_name}, добавлен в {new_class}{alphabet_class} класс')
        print(classes)

def delete():
    new_name = str(input('Введите имя ученика, которого хотите удалить: ')).lower()
    search_result = search(new_name)
    if search_result:
        class_key, alphabet, pupil_name = search_result
        classes[class_key][alphabet].pop(pupil_name)
        print(f'Ученик {pupil_name} был удален.')
    else:
        print('Такого имени нет в списке')
    print(classes)

def redact():
    menu1 = str(input('Выберите действие, которое хотели бы сделать:\n\n'
                      '1 - Редактировать Ф.И.О. ученика\n'
                      '2 - Редактировать номер ученика\n'))
    if menu1 == '1':
        old_name = str(input('Введите Ф.И.О. ученика, которого хотели бы отредактировать: ')).lower()
        search_result = search(old_name)
        if search_result:
            class_key, alphabet, pupil_name = search_result
            new_name = str(input('Введите имя, на которое хотели бы заменить имя ученика: '))
            classes[class_key][alphabet][new_name] = classes[class_key][alphabet].pop(pupil_name)
            print(f'Ф.И.О. ученика изменено на {new_name}.')
        else:
            print('Такого имени нет в списке')
        print(classes)
    elif menu1 == '2':
        old_name = str(input('Введите Ф.И.О. ученика, номер которого хотите отредактировать: ')).lower()
        search_result = search(old_name)
        if search_result:
            class_key, alphabet, pupil_name = search_result
            new_number = str(input('Введите новый номер ученика: '))
            classes[class_key][alphabet][pupil_name] = new_number
            print(f'Номер телефона ученика {pupil_name} изменен на {new_number}.')
        else:
            print('Такого имени нет в списке')
        print(classes)

keys1 = ['1', '2', '3', '4']
keys2 = ['A', 'B', 'C', 'D', 'E', 'F']
classes = {key: {} for key in keys1}
for clase in classes:
    classes[clase] = {i: {} for i in keys2}
while True:
    menu = str(input('Выберите действие: \n\n'
                     '1 - Добавить ученика\n'
                     '2 - Удалить ученика\n'
                     '3 - Изменить Ф.И.О. или номер ученика\n'))
    if menu == '1':
        add()
    elif menu == '2':
        delete()
    elif menu == '3':
        redact()
    else:
        print('Такой функции не существует')