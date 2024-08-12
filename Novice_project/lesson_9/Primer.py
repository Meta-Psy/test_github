class MyClass:
    def __init__(self, value):
        self.value = value
    @classmethod
    def from_string(cls, string):
    # Берем строку и переводим в числовые значения
        return cls(int(string))

my_obj = MyClass.from_string("10")
print(my_obj.value) #Вывод 10