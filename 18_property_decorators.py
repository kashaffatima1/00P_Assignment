# 18. Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price must be greater than zero")
        
    @price.deleter
    def price(self):
        del self._price

p1 = Product(1000)
print(p1.price) 

p1 = Product(9000) 
print(p1.price)

del p1.price
