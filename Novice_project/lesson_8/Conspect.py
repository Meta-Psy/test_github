# ООП:          1. Классы;          2. Объекты;         3. Атрибуты;    4. Методы
# Концепции:    1. Наследование;    2. Инкапсуляция;    3. Полиморфизм; 4. Интерфейс -> абстракция
# Класс - анкета. Объект - человек, который заполняет анкету. Атрибут - строчки в анкете (характеристики). Методы - обязанности человека после вступления на должность
# Концепции:
# 1. Инкапсуляция - объединение атрибутов и методов в единый модуль - класс.
# Преимущества: "инкапсулирует" сам шаблон для объектов. Доступ к этому шаблону, прописывается через методы.
# Иным способом же, кроме как через продуманный интерфейс (методы) получить доступ к этому шаблону невозможно
# 2. Наследование - создание производных классов от базового.
# Преимущества: можно создать производный класс, который "унаследует" все особенности родительского суперкласса и приобретет свои особенности
class GrandParent:
    def __init__(self):
        print("GrandParent init")
class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        print("Parent init")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")         # Вывод: # GrandParent init  # Parent init   # Child init

# 3. Полиморфизм - поволяет использовать объекты разных классов через единый интерфейс.
# Преимущество: можно использовать один и тот же метод, но для выполнения разных действий (в зависимости от того, к какому классу обращается метод)
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
def make_animal_speak(animal):
    print(animal.speak())           # Происходит замена функции speak в зависимости от обращения к dog или cat

# 4. Абстракция - выделяет значимые детали, и позволяет использовать их свободно в подклассах
# Преимущества: Позволяет выделить функцию, которая есть во всех подклассах и работать только с ней, однако, в отличии от полиморфизма,
# не требует наличия команды во всех подклассах без исключения
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"              #

class User:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

class Car:
    type = 'Bugatti'
    color = 'White'
    max_speed = 300
# __init__ инициализация. Вызывается сама по себе (по умолчанию)
class Person:
    def __init__(self, name, gender, age=0):
        self.name = name
        self.gender = gender
        self.age = age
person1 = Person('Aleksey, male, year')     # Создание объекта
print(person1.gender)                       # Обращение к атрибуту объекта (достаточно написать без скобок)
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes
comment1 = Comment('Alex', 'Hello')
print(vars(comment1))                       # Позволяет использовать
print(comment1.username)
