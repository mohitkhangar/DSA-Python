n = 4

for i in range(n):
    for j in range(i+1):
        print(j+1 , end = "")
    for j in range((n-i-1)*2):
        print("|", end = "")

    for j in range(i+1, 0, -1):
        print(j, end = "")

    print()