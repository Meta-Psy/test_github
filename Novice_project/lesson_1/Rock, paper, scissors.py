#Игрок 1
player1 = str(input('Выберите "Камень (К)", "Ножницы" (Н), "Бумага" (Б): '))
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')
print('{}')

#Игрок 2
player2 = str(input('Выберите "Камень (К)", "Ножницы" (Н), "Бумага" (Б): '))

#Игра
if(player1 == player2):
    print('Ничья!')
elif(player1 == 'К' and player2 == 'Б' or player1 == 'Н' and player2 == 'К' or player1 == 'Б' and player2 == 'Н'):
    print('Выиграл Игрок 2!')
else:
    print('Выиграл Игрок 1!')