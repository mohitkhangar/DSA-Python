class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def total_objects(cls):
        return cls.count

Counter()
Counter()
print(Counter.total_objects())


