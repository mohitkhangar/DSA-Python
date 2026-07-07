def print0toN(i,n):
    if i > n:
        return
    print(i)
    print0toN(i + 1, n)

print0toN(1,6)
