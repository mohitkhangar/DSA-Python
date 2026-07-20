class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        # Check every adjacent pair (including last -> first)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        # A sorted & rotated array can have at most one break
        return count <= 1
