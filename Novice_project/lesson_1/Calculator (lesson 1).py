a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = str(input("Укажите какое действие необходимо сделать"))
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    if b != 0:
        print(a/b)
    else:
        print("Деление на 0 невозможно")
else:
    print("Не правильно введен оператор!")
