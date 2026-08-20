def decorators(func):
    def wrapper():
        print("I am about to execute the function")
        func()
        print("function is executed")
    return wrapper()
        




def say_hello():
    print("hello!")
f = decorators(say_hello)
f()
    