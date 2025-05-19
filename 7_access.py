# 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name 
        self._salary = salary
        self.__ssn = ssn

emp1 = Employee("Aliyar", 50000, "123-45-6789")
print(emp1.name) 
print(emp1._salary) 
print(emp1._Employee__ssn) #123-45-6789
print(emp1.__ssn) #Attribute Error
