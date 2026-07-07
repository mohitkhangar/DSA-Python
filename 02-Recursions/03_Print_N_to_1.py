def printNto0(i,n):
    if n==0:
        return
    print(n)
    printNto0(i,n-1)
printNto0(1,6)