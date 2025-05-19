# 14. Aggregation

class Employee:
    def __init__(self, name):
        self.name = name
    def get_details(self):
        return f"Employee name: {self.name}"
       
class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee
    def get_depart_details(self):
        return f"Department name: {self.name},\n{self.employee.get_details()}"

emp1 = Employee("Kashaf")
dept1 = Department("Maths Teacher", emp1)
print(dept1.get_depart_details())