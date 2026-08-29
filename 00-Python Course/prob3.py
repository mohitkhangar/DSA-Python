logged_in = True
def login_required(func):
        def wrapper():
            if logged_in:
                func()
            else:
                print("You are not logged in")
        return wrapper
@login_required
def hello():
        print("Hello World")
hello()
