arr = [1, 8, 7, 56, 90]

n = len(arr)

Largest = arr[0]

for i in range(1,n):
    if arr[i] > Largest:
        Largest = arr[i]

print("The largest element in the array is:", Largest)