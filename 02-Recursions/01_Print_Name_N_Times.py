def printName(n):
    if n == 0:
        return
    print("Mohit")
    printName(n - 1)

printName(5)