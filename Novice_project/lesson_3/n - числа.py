number = float(input('Введите любое число: '))
round_number = round(number, 0)
a = int(round_number)
count = 0
for num in range(1, a, 1):
    count += num
print(f'Сумма всех натуральных положительных числе = {count}')
