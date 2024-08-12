dif_vol = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2, 5, 18, 20]
summ = 0
for bottles in dif_vol:
    num = int(input(f'Какое количество бутылок "{bottles}" размера вы сдаёте: '))
    if bottles <= 1.00:
        summ += 0.10 * num
    elif bottles > 1.00:
        summ += 0.25 * num
itogo = round(summ, 2)
print(f'Вы выручите {itogo} $ за ваши бутылки')
