names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
answer = [p[0] for p in names]

print(answer)

numbers = [a for a in range(1, 21, 1)]
nums2 = [num for num in numbers if num % 2 == 0]

print(nums2)

usernames = ['Олег']
while True:
    name = input('Введите имя: ')
    if name.lower() in [i.lower() for i in usernames]:
        print('Имя занято')
    else:
        usernames.append(name)
        print(f'{name} добавлен в список контактов')
        print(usernames)

# TODO УДАЛИТЬ ПРОЕКТ
