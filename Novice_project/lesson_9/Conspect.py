# Наследование
class Animal:
    def eat(self):
        print(f'{self} кушает')

class Mamal(Animal):
    def milk_feed(self):
        print(f'{self} кормит молоком')

class Horse(Mamal):
    def jump(self):
        print(f'{self} прыгает')

horse1 = Horse()
horse1.milk_feed()

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

class SuperCar(Car):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor

class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1, Parent2):
    pass

class MyClass:
    @classmethod                                    # делает метод доступным через класс, а не через экземпляр
    def class_info(cls):
        return f'This is the {cls.__name__} class'

print(MyClass.class_info())

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property                                       # Превращает метод в атрибут, позволяя обращаться к нему без вызова скобок
    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 5)
print(rectangle.area)

rectangle.width = 6
print(rectangle.area)

