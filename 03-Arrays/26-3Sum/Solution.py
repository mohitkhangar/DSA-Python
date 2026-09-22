class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range( j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        return [list(x) for x in result]
