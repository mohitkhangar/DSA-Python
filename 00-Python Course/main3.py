while True:
    try:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(f"The Division in {a/b}")

    except ValueError:
        print("Please don't perform bad typecasts ")
    except ZeroDivisionError:
        print("Hey! don't divide by zero")

    except Exception as e:
        print("Some error occured", e)

