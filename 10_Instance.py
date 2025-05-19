# 10. Instance Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Coco", "Golden Retriever")
dog2 = Dog("Max", "Poodle")
dog1.bark()
dog2.bark()