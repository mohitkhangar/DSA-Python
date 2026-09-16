items = ["apple", "banana", "apple", "orange", "banana", "apple"]
target = "apple"

count = 0 

for item in items:
    if item == target:
        count += 1
print(f' {target} appears {count} times')