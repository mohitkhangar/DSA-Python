import time
from os import times_result


def timer(func):
    start = time.time()
    func()
    end = time.time()
    print("time taken: ", end - start)
    return func
@timer
def test():
    for i in range(1000000):
        pass

test()

