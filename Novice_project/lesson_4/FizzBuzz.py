numbers = list(range(1, 100))
Fizz_Buzz = []
for x in numbers:
    ind = numbers.index(x)
    if x % 3 == 0 and x % 5 == 0:
        numbers[ind] = 'FizzBuzz'
    elif x % 5 == 0:
        numbers[ind] = 'Buzz'
    elif x % 3 == 0:
        numbers[ind] = 'Fizz'
print(numbers)






