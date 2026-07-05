"""
╔══════════════════════════════════════╗
║  LeetCode #1 — Two Sum              ║
║  Difficulty: Easy                    ║
║  Topic: Arrays, HashMaps            ║
║  Striver A2Z: Step 3 - Arrays       ║
╠══════════════════════════════════════╣
║  Time:  O(n)                        ║
║  Space: O(n)                        ║
╚══════════════════════════════════════╝

Problem:
Given array of integers and target,
return indices of two numbers that add to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]  (nums[0] + nums[1] = 9)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

# ── Test ──────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))         # [1, 2]
    print(sol.twoSum([3, 3], 6))            # [0, 1]

# ── AI/ML Connection ──────────────────
# HashMap lookup = same concept used in
# embedding lookup tables in NLP models
# and feature indexing in recommendation systems
