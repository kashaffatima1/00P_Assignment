# 13. Composition

class Engine:
    def start(self):
        print("Engine started!!")
        
        
class Car:
    def __init__(self, engine):
        self.engine = engine
        
    def car_start(self):
        return self.engine.start()

eng = Engine()
my_car = Car(eng)
my_car.car_start()

