def linear_search(arr, target):
    """
    Performs Linear Search on the given array.

    Parameters:
        arr (list): List of elements.
        target (int): Element to search.

    Returns:
        int: Index of the target if found, otherwise -1.
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# Driver Code
arr = [12, 45, 7, 23, 56, 89, 34]
target = 23

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
