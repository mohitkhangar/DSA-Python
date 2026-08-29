def even_only(func):
    def wrapper(n):
        if n % 2 == 0:
            func(n)
        else:
            print("Only even numbers allowed")
    return wrapper

@even_only
def show(n):
    print(n)

show(4)
show(5)
