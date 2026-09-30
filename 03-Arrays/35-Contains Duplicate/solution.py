class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            while nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k :
                window.remove(nums[i-k])
        return False
