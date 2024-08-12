class Student:

    def __init__(self,name = 'Ivan', groupNumber = '10 A', age = 18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

    def getgroupNumber(self):
        print(self.groupNumber)

    def setNameAge(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def setGroupNumber(self, new_number):
        self.groupNumber = new_number

student1 = (Student('Ami', '11A', 13))
student2 = (Student('Rei', '11B', 14))
student3 = (Student('Makoto', '11C', 15))
student4 = (Student('Minako', '11D', 16 ))
student5 = (Student('Usagi', '11E', 17))
student = (Student())

print(vars(student))
print(vars(student1))