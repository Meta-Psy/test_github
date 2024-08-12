# Dictionary
x = {'name': 'Pasha', 'job': 'TGbot creator'}
print(x['name'])
# Можно вызвать 3 метода, для вызова конкретной части словаря
my_dict = {'names': ['Jordan', 'Pavel', 'Sasha'],
           'user': 'Pasha',
           'numbers': (99, 80)}
a = list(my_dict.values())
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())
print(a)
#
if 99 in my_dict.items():                              # По умолчанию, посик идет по ключам словаря
    print('Да, есть')
else:
    print('Не понимаю о чем вы')
print(list(my_dict.items()))

my_dict['gender'] = ['male']
print(my_dict)

cafees = {'Evos': {'Gorod': 'Tashkent', 'Filialov': 'Много', 'Otkritie': 2007}}
cafees['Evos']['кухня'] = 'Fast Food'
print(cafees)

instructor = {'name': 'Jordan'}
instructor['name'] = [instructor['name'], 'Pasha']
print(instructor)

instructor['name'].append('Oleg')
print(instructor)

# Методы удаления
my_dict.popitem()

my_dict.clear()
print(my_dict)

a = {}.fromkeys('a', 1)
print(a.get)

a = dict(name='Jordan', age='12')
print(a)

instr = dict(name='Jordan', age=32, job='Python developer')

for k, v in instr.items():
    print(k, v)

