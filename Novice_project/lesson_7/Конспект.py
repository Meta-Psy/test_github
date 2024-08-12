# Библиотеки: 1. Встроенные; 2. Не встроенные
# pip install requests - скачивает новую библиотеку (в данном случае requests)
# pip freeze           - показывает уже установленные библиотеки
# pip install -r requirements.txt Перед этим, нужно создать файл requirements.txt. Устанавливает все библиотеки в файле requirements.txt
# pip freeze > requirements.txt - анализирует все библиотеки, которые были использованы для создания данного проекта

import requests                 # Импортирует все команды в проект, из указанной библиотеки (в данном случае requests)
from requests import get      # Можно импортировать только одну функцию из всей библиотеки
from Novice_project.lesson_6.School_management_system import add      # Можно импортировать только одну функцию из собственных программ
get('a')
add()

# Парсинг
import requests
url = 'https://tma.uz'        # Создаем переменную с адресом сайта
response = requests.get(url)  # При помощи команды get из библиотеки requests, псоздаем переменную с данными url
print(response.text)          # Снова при помощи библиотеки requests выводим url в виде текста. Это и есть парсинг

# lambda. Временная переменная
a = lambda x: x**2            # Не требует собственного названия. Можно написать все в одну строчку
print(a(19))

def primer_lambda(x):         # Тоже самое, только при помощи функции "def"
    return x+1

a = lambda x, y: 2*(x+y)      # Так же можно указывать несколько переменных, через запятую, далее используя их всех
print(a(2, 4))

# map
primer = [3, 4, 6, 7, 44, 3]  # Можно воспользоваться существующим списком с множеством элементов. Лямбда примет их за параметры, по-очереди)
a = map(lambda x: x + 2, primer)
print(list(a))

# filter                      # Тоже самое, что if, только для lambda
b = filter(lambda d: d*2 == 4, primer)
print(list(b))

primer2 = [1, 2, -4, -4, -8, -7, 4, 15, 18, 19, 21, -98]
y = filter(lambda a: a >= 0, primer2)
print(list(y))