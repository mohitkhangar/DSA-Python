from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        result = []

        for right in range(len(nums)):

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            # Remove elements outside window
            if dq[0] <= right - k:
                dq.popleft()

            # Window formed
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result
