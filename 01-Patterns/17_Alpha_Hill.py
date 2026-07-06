n = 5

for i in range(n):

    # Spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Left Part
    for j in range(i + 1):
        print(chr(ord('A') + j), end="")

    # Right Part
    for j in range(i - 1, -1, -1):
        print(chr(ord('A') + j), end="")

    print()