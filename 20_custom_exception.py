# 20. Creating a Custom Exception

class InvalidageError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
          raise InvalidageError(f"Invalid age: {age}")
    else:
        print(f"Age is valid: {age}")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidageError as e:
    print(e.message)
except ValueError:
    print("Invalid input. Please enter a valid age.")