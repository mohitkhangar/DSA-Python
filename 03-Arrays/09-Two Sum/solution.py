class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            result = target - num
            if result in hashmap:
                 return[hashmap[result], i]
            hashmap[num]=i

