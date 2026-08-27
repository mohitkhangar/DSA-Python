while True:
    try:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(f"The Sum in {a+b}")
    except Exception as e:
        print("Some error occured", e)