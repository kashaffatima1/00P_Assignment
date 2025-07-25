# 21. Make a Custom Class Iterable

class Countdown:
    def __init__(self, starts):
        self.starts = starts
        self.current = starts

    def __iter__(self):
       return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
    
for number in Countdown(5):
    print(number)
print("Jet off!")

