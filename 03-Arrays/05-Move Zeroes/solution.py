class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
