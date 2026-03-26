
from abc import ABC,abstractmethod

class Student(ABC):
    class_year=2025

    def __init__(self,name,surname,age,major):
        self.name=name
        self.surname=surname
        self.age=age
        self.major=major

    @abstractmethod
    def succeed(self):
        pass
    @abstractmethod
    def fail(self):
        pass

class Girl(Student):
    def succeed(self):
        return 1
    def fail(self):
        return 0

class Boy(Student):
    def succeed(self):
        return 1
    def fail(self):
        return 0

boy=Boy('Nurlan','Zamanov',18,'CE')
girl=Girl('Meg','Ryan',30,'Actress')

print(girl.fail())


        
