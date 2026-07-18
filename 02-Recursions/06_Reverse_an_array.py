lst = list(map(int, input().split()))

s = 0
e = len(lst) - 1

while s < e:
    lst[s], lst[e] = lst[e], lst[s]
    s += 1
    e -= 1

print(lst)
