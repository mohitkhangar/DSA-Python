a = int(input("enter a number between 1 and 10: "))

match a:
    case 1:
        print("you won a charger")
        
    case 2:
        print("you won 3$")
        
    case 3:
        print("you won a game")
    
    case _:
        print("better luck next time")