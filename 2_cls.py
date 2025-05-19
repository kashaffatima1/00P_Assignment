# 2. Using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total instances created: {cls.count}")

c1 = Counter()
c2 = Counter()
c1.show_count() 
    