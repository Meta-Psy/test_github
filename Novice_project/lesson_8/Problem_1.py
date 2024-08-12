class Student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age
        return name, age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber
        return groupNumber

# Создание пяти экземпляров класса Student с различными значениями атрибутов
student1 = Student('Alex', 24, '18A')
student2 = Student('Sardor', 26, '18B')
student3 = Student('Rakhshona', 25, '18C')
student4 = Student('Ahror', 25, '18D')
student5 = Student('Suhrob', 30, '18E')

print(student1.getName())
print(student2.getAge())
print(student3.getGroupNumber())
print(student4.setNameAge('Botir', 20))
print(student5.setGroupNumber('13B'))