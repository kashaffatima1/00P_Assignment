# 8. The super() Function

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

T1 = Teacher("Kashaf", "Math")
print(T1.name, T1.subject)  