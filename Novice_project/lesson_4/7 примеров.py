numbers = list(range(1, 100))
numbers_FizzBuzz = ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else x for x in numbers]
numbers_Fizz = ['Fizz' if x % 5 == 0 else x for x in numbers]
numbers_Buzz = ['Buzz' if x % 3 == 0 else x for x in numbers]
numbers_FizzBuzz_Fizz = numbers_FizzBuzz.extend(numbers_Fizz)
print(numbers_FizzBuzz_Fizz)