def count_call(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("called",count,"times")
        func()
    return wrapper
@count_call
def hello():
    print("Hello")
hello()
hello()
