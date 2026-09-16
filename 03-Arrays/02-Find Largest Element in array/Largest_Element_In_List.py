numbers  = [12, 45, 7, 89, 34, 23]

largest = numbers[0]
for element in numbers[1:]:
    if element > largest:
        largest = element
print(f'Largest Element: {largest}')

    