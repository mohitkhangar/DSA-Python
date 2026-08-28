try:
    a=int(input("enter the first number "))
    b=int(input("enter the second number 89"))

    print("What kind of operation do you wanna perform. Press + for addition\nPress - for subtraction\nPress / for division\nPress * for multiplication ")

    o = input("Enter operation:")
    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "/":
            print(f"The result is: {a / b}")
        case "*":
            print(f"The result is: {a * b}")
        case default:
            print(f"There was an error")

except Exception as e:
    print("Enter the valid value of a and b")
    
    
    
