words = ['о', 'в', 'о']
word = words.reverse()
print(word)
# Примеры работы for in
for item in 'Alex':
    print(item)
nabor = ('1', 2, 'a')
for b in nabor:
    print(b)
p = ['m', 'my', 23]
for tor in p:
    print(tor)

# Пример ошибки
#for primer in (6, 4, '2'):
    #print (primer+2)

# Пример повторения цикла
my_tuple = (6, 4, '2')
count = 0
for i in range (1, 100):
    print(my_tuple)
    count += 1
print(count)

my_tuple = (6, 4, '2')
count = 0
for i in range (1, 100, 2):
    print(my_tuple)
    count += 1
print(count)

# Цикл while
spam = 'Hello'
while spam == 'Hello':
    print(spam)

while 'a' in nabor:
    print('it is')

p = ['m', 'my', 23]
i = 0
while i < 0:
    print(p[i])
    i = i + 1
for i in p:
    print(i)

names = ['Ivan', 'Pavel', 'Jordan']
while True:
    new = input('Кого добавим?')
    if new == 'Список':
        print(names)
    else:
        names.append(new)
        print(f'{new} добавлен')