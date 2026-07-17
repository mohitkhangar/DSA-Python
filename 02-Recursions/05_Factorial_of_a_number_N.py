def fact(i,n):
    if i > n:
        return 1
    return i*fact(i+1,n)

ans = fact(1, 5)
print(ans)