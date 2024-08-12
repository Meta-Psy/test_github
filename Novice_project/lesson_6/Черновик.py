def new_function():
    print('Hello World')
new_function()

def create_list():
    my_list = []
    return my_list

create_list()
print(create_list())

def spam2(a):
    print(a+6)
spam2(23)

def calc(a, b, c=7):
    print(a+b)
    return
calc

def square(a, b):
    return a * b
print(square(2, 4))

def spam1(*args):
    return args
print(spam1(1, 2, 3, 'Hello'))

def spam1(**kwargs):
    return kwargs

print(spam1(name='my1', age=23))

def spam1(**kwargs):
    for k, v in kwargs.items():
        return k, v
print(spam1(name='my1', age=23))
