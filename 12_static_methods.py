# 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
temp1 = TemperatureConverter()
print(temp1.celsius_to_fahrenheit(45))
temp2 = TemperatureConverter()
print(temp2.celsius_to_fahrenheit(22))