def chet_nechet(*args):
    chet = []
    nechet = []
    for x in args:
        if x % 2 == 0:
            chet.append(x)
        elif x % 2 != 0:
            nechet.append(x)
    return chet.extend(nechet)
while True:
    args = str(input('Введите числа '))
    print(chet_nechet())

