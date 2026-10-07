# 209. Minimum Size Subarray Sum

🔗 LeetCode: 209. Minimum Size Subarray Sum  
🟡 Difficulty: Medium  
🏷️ Pattern: Variable Size Sliding Window

---

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If there is no such subarray, return `0`.

---

## Example

### Input

```text
target = 7
nums = [2,3,1,2,4,3]
```

### Output

```text
2
```

### Explanation

The subarray `[4,3]` has sum `7` and length `2`, which is the smallest possible valid subarray.

---

## Intuition

Since all numbers are **positive**, the window sum:

- Increases when we move `right`
- Decreases when we move `left`

This allows us to use a **variable-size sliding window**.

### Strategy

1. Expand the window by moving `right`.
2. Keep adding elements to `window_sum`.
3. Once `window_sum >= target`:
   - Update the minimum length.
   - Shrink the window from the left.
4. Continue until all elements are processed.

---

## Sliding Window Visualization

```text
target = 7

[2,3,1,2] = 8 ✓
length = 4

Shrink:

[3,1,2] = 6 ✗

Expand:

[3,1,2,4] = 10 ✓
length = 4

Shrink:

[1,2,4] = 7 ✓
length = 3

Shrink:

[2,4] = 6 ✗

Expand:

[2,4,3] = 9 ✓
length = 3

Shrink:

[4,3] = 7 ✓
length = 2
```

Answer = **2**

---

## Optimal Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)

                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
```

---

## Why This Works

When the window sum becomes at least `target`, the current window is valid.

Instead of stopping there, we try to shrink it because a smaller valid window may exist.

Since all numbers are positive:

```text
Move right  -> Sum increases
Move left   -> Sum decreases
```

Therefore every element enters and leaves the window at most once.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each element is:

- Added once
- Removed once

Total operations ≤ 2n.

### Space Complexity

```text
O(1)
```

Only a few variables are used.

---

## Pattern Recognition

Use **Variable Size Sliding Window** when:

- Looking for smallest/longest subarray
- Condition depends on sum/count
- Array contains positive integers
- Window can expand and shrink dynamically

Common keywords:

- Minimum length subarray
- Smallest window
- Sum ≥ target
- Continuous subarray
- Positive integers

---

## Sliding Window Template

```python
left = 0

for right in range(len(nums)):

    # Expand window
    add nums[right]

    while window is valid:

        update answer

        # Shrink window
        remove nums[left]
        left += 1
```

---

## Key Takeaway

Whenever you see:

- Positive numbers
- Subarray
- Minimum length
- Sum condition

Think:

👉 **Variable Size Sliding Window**

This problem is one of the most important sliding window patterns and appears frequently in coding interviews.
