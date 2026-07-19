def largestElement(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


nums = list(map(int, input("Enter array elements: ").split()))

print("Largest Element:", largestElement(nums))
