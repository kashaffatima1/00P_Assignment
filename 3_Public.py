# 3.Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"Brand: {self.brand}")
    
my_car = Car("Toyota")
print(my_car.brand)
my_car.start()  