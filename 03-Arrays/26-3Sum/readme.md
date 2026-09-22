# 15. 3Sum

## Problem Statement

Given an integer array `nums`, return all the triplets:

- `nums[i] + nums[j] + nums[k] == 0`
- `i != j`, `i != k`, `j != k`

The solution set must not contain duplicate triplets.

### Example

Input:

```python
nums = [-1,0,1,2,-1,-4]
```

Output:

```python
[[-1,-1,2],[-1,0,1]]
```

---

## Approach

### Brute Force

Check every possible triplet using three nested loops.

- Time Complexity: `O(n³)`
- Space Complexity: `O(1)`

This approach is too slow for large inputs.

---

## Optimized Approach (Sorting + Two Pointers)

### Idea

1. Sort the array.
2. Fix one element `nums[i]`.
3. Use two pointers:
   - `left = i + 1`
   - `right = n - 1`
4. Calculate:

```python
total = nums[i] + nums[left] + nums[right]
```

- If `total == 0`, store the triplet.
- If `total < 0`, move `left` forward.
- If `total > 0`, move `right` backward.
- Skip duplicates to avoid repeated triplets.

---

## Algorithm

1. Sort the array.
2. Iterate through each element.
3. Skip duplicate starting elements.
4. Use two pointers to find pairs whose sum equals `-nums[i]`.
5. Store valid triplets.
6. Return the result.

---

## Python Solution

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
```

---

## Complexity Analysis

### Time Complexity

- Sorting: `O(n log n)`
- Two-pointer traversal: `O(n²)`

Overall:

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

(Excluding the output array)

---

## Key Concepts Learned

- Sorting
- Two Pointers
- Duplicate Handling
- Array Traversal
- Optimization from O(n³) to O(n²)

---

## Pattern

This problem follows the:

**Two Pointer + Sorting Pattern**

Common related problems:

- Two Sum II
- 3Sum Closest
- 4Sum
- Container With Most Water
