# Assignment 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice

# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}\nMarks: {self.marks}")

s1 = Student("Eisha", 90)
s1.display()