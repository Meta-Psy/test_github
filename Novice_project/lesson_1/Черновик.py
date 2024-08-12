# Общая информация
a = float(input('Введите число: '))
if(a % 1 == 1):
    number = (a // 1) + 1
    print(round(number))
else:
    print(round(a))
print(round(2.45, 2))