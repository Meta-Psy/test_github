password = str(input('Введите пароль: '))
def new_password():
    password_new = str(input('Введите новый пароль'))
    return password_new
def num_len(password):
    if len(password) < 8:
        print('Пароль должен содержать минимум 8 символов')
        return new_password()
    elif len(password) > 17:
        print('Пароль должен содержать максимум 17 символов')
        return new_password()
    else:
        return password

def num_have(password):
    nums = range(0,10)
    if str(nums) not in password:
        print('Пароль должен содержать как минимум одну цифру')
        return new_password()
    elif str(nums) not in password:
        return password

def symbols(password):
    for i in password:
        if not i.isdigit() or not i.isalpha() or 'i' != i:
            return 'Нельзя использовать любые символы, кроме _'

def all():
    num_len(password)
    num_have(num_len)
    true_password = symbols(num_have)
    return true_password

all()
print(f'Ваш пароль {all()} соответствует всем нормам')
