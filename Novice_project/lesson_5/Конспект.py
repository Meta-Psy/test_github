# Словарь                                Много ключей, имеющих своё "значение". Однако значения должны быть упакованы в list, tuple, str, dict
my_dict = {'names': ['Jordan', 'Pavel', 'Sasha'],
                                        'user': 'Pasha',
                                        'numbers': (99, 80)}
# Методы словарей
my_dict.keys()                          # Выдает каждый из ключей. По умолчанию и так стоит работа с ключами
my_dict.values()                        # Выдает все значения, каждого из ключей
my_dict.items()                         # Выдает ключ + значение

# Функции замены:
my_dict2 = {'name': 'Jordan'}
my_dict2['name'] = 'Pasha'              # my_dict2 = {'name': 'Pasha'}

# Функции добавления:
# Классическое
users = {}
users['name'] = 'Jordan'                # users = {'name': 'Jordan'}
# В словарь словаря
cafees = {'Evos': {'Gorod': 'Tashkent', 'Filialov': 'Много', 'Otkritie': 2007}}
cafees['Evos']['кухня'] = 'Fast Food'   # cafees = {'Evos': {'Gorod': 'Tashkent', 'Filialov': 'Много', 'Otkritie': 2007, 'кухня': 'Fast Food'}}
# Добавление-Замена... По сути замена, с учетом старых данных. По итогу - добавление новых значений, в лист
instructor = {'name': 'Jordan'}
instructor['name'] = [instructor['name'], 'Pasha']
# В словарь, с типом данных значений list
instructor['name'].append('Oleg')

# Функции удаления
instructor.clear()                      # удаляет все из словаря
instructor.pop('name')                  # удаляет 1 ключ:значение, указанного в скобках
instructor.popitem()                    # удаляет 1 ключ:значение, самый последний в словаре

# Функции создания нового словаря       # Можно создать множество ключей, однако у всех будет только одно значение
{}.fromkeys('a', 1)
print({}.fromkeys(['song'], 'Godzilla'))

keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys)          # {'a': None, 'b': None, 'c': None}

keys = ('a', 'b', 'c')
value = []
new_dict = dict.fromkeys(keys, value)   # {'a': [], 'b': [], 'c': []}

items = ['apples', 'bananas', 'oranges']
inventory = {item: [] for item in items}# Чтобы эта функция стала полезной, ей нужно задать нулевые значения, перед началом использования
inventory['apples'].append(5)
inventory['bananas'].append(3)
print(inventory)

a = dict(name='Jordan', age='12')
print(a)

# Получить информацию о словаре:
inventory.get('items')                  # Выдает все значения указанного ключа

# Сеты                                  # Рандомная сортировка каждый раз, убирает все дупликаты при использовании. Индексы элементов так же убираются
nums = {1, 2, 3, 3, 4, 4, 5}
print(nums)                             # 1, 2, 3, 4, 5

# Взаимодействие с циклом for
for k in inventory.keys():
    print(k)

for v in inventory.values():
    print(v)

for k, v in inventory.items():
    print(k, v)
