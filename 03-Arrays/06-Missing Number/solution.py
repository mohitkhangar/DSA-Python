class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        correct_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return correct_sum - actual_sum
