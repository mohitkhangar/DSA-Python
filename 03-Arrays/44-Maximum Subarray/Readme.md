# 53. Maximum Subarray

## Problem Statement

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

---

## Intuition

At each position, we decide:

1. Continue the previous subarray.
2. Start a new subarray from the current element.

If the running sum becomes negative, carrying it forward will only reduce future sums. Therefore, we start a new subarray whenever starting fresh is better.

This idea leads to Kadane's Algorithm.

---

## Approach (Kadane's Algorithm)

Maintain:

- `current_sum` → Maximum subarray sum ending at current index.
- `max_sum` → Best subarray sum found so far.

For each element:

```python
current_sum = max(nums[i], current_sum + nums[i])
```

Update:

```python
max_sum = max(max_sum, current_sum)
```

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
```

---

## Dry Run

Input:

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

Progress:

| Num | Current Sum | Max Sum |
|------|------------|----------|
| -2 | -2 | -2 |
| 1 | 1 | 1 |
| -3 | -2 | 1 |
| 4 | 4 | 4 |
| -1 | 3 | 4 |
| 2 | 5 | 5 |
| 1 | 6 | 6 |
| -5 | 1 | 6 |
| 4 | 5 | 6 |

Output:

```text
6
```

Subarray:

```text
[4, -1, 2, 1]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Single traversal of the array.

### Space Complexity

```text
O(1)
```

Only two variables are used.

---

## Pattern Recognition

- Dynamic Programming
- Kadane's Algorithm
- Greedy Optimization
- Maximum Subarray Problems

---

## Key Takeaway

At every index:

```python
current_sum = max(nums[i], current_sum + nums[i])
```

Either:

- Extend the current subarray
- Start a new subarray

Choose the option with the larger sum.
