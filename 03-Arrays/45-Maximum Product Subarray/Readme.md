# 152. Maximum Product Subarray

## Problem Statement

Given an integer array `nums`, find a contiguous subarray that has the largest product and return that product.

A subarray must contain consecutive elements from the original array.

### Example 1

**Input**
```python
nums = [2, 3, -2, 4]
```

**Output**
```text
6
```

**Explanation:** The subarray `[2, 3]` has the maximum product, which is `2 × 3 = 6`.

### Example 2

**Input**
```python
nums = [-2, 0, -1]
```

**Output**
```text
0
```

**Explanation:** The maximum product comes from the subarray `[0]`.

---

## Approach: Dynamic Programming

The main challenge is handling negative numbers.

In a product-based problem, multiplying by a negative number can change a large positive product into a negative product. Similarly, multiplying a large negative product by another negative number can produce a large positive product.

Therefore, we maintain three variables:

- `current_max`: Maximum product of a subarray ending at the current position.
- `current_min`: Minimum product of a subarray ending at the current position.
- `max_product`: Maximum product found anywhere in the array.

### Algorithm

1. Initialize all three variables with the first element of the array.
2. Traverse the remaining elements.
3. If the current number is negative, swap `current_max` and `current_min`.
4. Calculate the new maximum product by either starting a new subarray or extending the previous maximum product.
5. Calculate the new minimum product similarly.
6. Update `max_product` whenever a larger product is found.
7. Return `max_product`.

---

## Python Solution

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            max_product = max(max_product, current_max)

        return max_product
```

---

## Dry Run

**Input**
```python
nums = [2, 3, -2, 4]
```

| Current Number | Current Maximum | Current Minimum | Overall Maximum |
|---:|---:|---:|---:|
| 2 | 2 | 2 | 2 |
| 3 | 6 | 3 | 6 |
| -2 | -2 | -12 | 6 |
| 4 | 4 | -48 | 6 |

**Output**
```text
6
```

The maximum-product subarray is `[2, 3]`, with a product of `6`.

---

## Why Do We Swap When the Number Is Negative?

Consider a previous maximum product of `6` and a minimum product of `-12`.

When multiplied by `-2`:

- `6 × (-2) = -12`
- `-12 × (-2) = 24`

The previous minimum product becomes the new maximum because a negative multiplied by a negative produces a positive.

That is why we swap `current_max` and `current_min` before updating them when the current number is negative.

---

## Complexity Analysis

- **Time Complexity:** `O(n)` — Each element is processed once.
- **Space Complexity:** `O(1)` — Only a constant number of variables are maintained.

---

## Key Concepts

- Dynamic Programming
- Maximum and Minimum Tracking
- Handling Negative Numbers
- Array Traversal
- Contiguous Subarrays

---

## Important Revision Notes

**Maximum Subarray (LeetCode 53):**
- Tracks the best running sum.
- Uses Kadane's Algorithm.

**Maximum Product Subarray (LeetCode 152):**
- Tracks both the maximum and minimum running products.
- Negative numbers can reverse which product is the maximum.
- Zero can break a product sequence, so starting a new subarray must always remain an option.

### Key Takeaway

For every element, decide whether to start a new subarray or extend the existing one. Track both the maximum and minimum products because negative values can change their roles.
