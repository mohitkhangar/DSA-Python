def isSorted(nums):
    n = len(nums)

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


nums = [1, 2, 3, 4, 5]
print(isSorted(nums))
