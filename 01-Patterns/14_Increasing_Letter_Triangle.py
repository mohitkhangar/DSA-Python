def numtochr(num):
    return chr(num + 65)

n = 5

for i in range(n):
    for j in range(i+1):
        print(numtochr(j), end = "")
        


    print()