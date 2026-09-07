s = input()
u = l = 0

for ch in s:
    if ch.isupper():
        u += 1
    else:
        ch.islower()
        l += 1

print("Upper:", u)
print("Lower:", l)
