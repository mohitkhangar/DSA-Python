def numtochr(num):
    return chr(num + 65)


n = 5
k = n - 1

for i in range (n):
    for j in range(i+1):
        print(numtochr(k+j),end="")

    k-=1
    print()