data = [4, 6, 2, 3, 1, 7, 5]

reverse_list = []

for i in range(len(data) - 1, -1, -1):
    reverse_list.append(data[i])
print(reverse_list)
