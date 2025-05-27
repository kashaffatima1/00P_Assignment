# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, number):
        return number * self.factor


multiply = Multiplier(4)
print(callable(multiply))
answer = multiply(5)
print(answer) 
