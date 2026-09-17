numbers = [1,2,2,3,4,4,5]

unique_elements = []
for number in numbers:
    if number not in unique_elements:
        unique_elements.append(number)
print(f'Unique_ELements:', unique_elements)