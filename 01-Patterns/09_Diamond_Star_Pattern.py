n = 5
for i in range(2*n):
    if i < 5:
        for j in range(n-i-1):
            print(" ",end='')
        for j in range((2*i)+1):
            print("*",end="")
    else:
        for k in range(i-n):
            print(" ",end='')
        for k in range(2*(n+n)-(2*i)-1):
            print("*",end="")
    print()