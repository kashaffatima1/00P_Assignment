# 17. Class Decorators

def add_greetings(cls):
    def greet(self):
        return "Hello from decorator!"
    cls.greet = greet
    return cls

@add_greetings
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Kashaf")
print(p1.greet())