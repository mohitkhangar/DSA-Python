# 219. Contains Duplicate II

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if there exist two distinct indices `i` and `j` such that:

```python
nums[i] == nums[j]
```

and

```python
abs(i - j) <= k
```

Otherwise, return `false`.

---

## Intuition

We need to check two conditions:

1. The values are the same.
2. Their indices are at most `k` positions apart.

A brute-force approach would compare every pair of elements.

```python
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] == nums[j] and abs(i-j) <= k:
            return True
```

This takes:

```python
O(n²)
```

which is too slow for large arrays.

Instead, we use a **Sliding Window + Hash Set**.

---

## Key Observation

For every element, we only care about the previous `k` elements.

Why?

Because if the distance exceeds `k`, the pair cannot satisfy:

```python
abs(i - j) <= k
```

So we maintain a window containing at most `k` recent elements.

If the current number already exists inside that window:

```python
Duplicate found within distance k
```

Return:

```python
True
```

Otherwise:

```python
Add current number to window
```

and continue.

---

## Sliding Window Idea

Example:

```python
nums = [1,2,3,1]
k = 3
```

Window:

```python
[1]
```

Add:

```python
2
```

Window:

```python
[1,2]
```

Add:

```python
3
```

Window:

```python
[1,2,3]
```

Current element:

```python
1
```

Already exists in window.

Distance:

```python
3
```

which is:

```python
<= k
```

Return:

```python
True
```

---

## Algorithm

1. Create an empty set.
2. Iterate through array.
3. If current element already exists in set:
   - Return `True`.
4. Add current element to set.
5. If window size becomes greater than `k`:
   - Remove the element that is now outside the window.
6. If traversal finishes:
   - Return `False`.

---

## Code

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False
```

---

## Dry Run

### Input

```python
nums = [1,2,3,1]
k = 3
```

Initial:

```python
window = {}
```

---

### i = 0

```python
nums[i] = 1
```

Not in set.

Add:

```python
window = {1}
```

---

### i = 1

```python
nums[i] = 2
```

Not in set.

Add:

```python
window = {1,2}
```

---

### i = 2

```python
nums[i] = 3
```

Not in set.

Add:

```python
window = {1,2,3}
```

---

### i = 3

```python
nums[i] = 1
```

Already exists in window.

Return:

```python
True
```

---

## Why Do We Remove Elements?

Consider:

```python
nums = [1,2,3,1]
k = 2
```

When we reach last `1`:

Valid window should only contain:

```python
[2,3]
```

because only the previous 2 elements matter.

The first `1` must be removed.

This is why:

```python
window.remove(nums[i-k])
```

keeps only relevant elements inside the window.

---

## Code Explanation

### Create Window

```python
window = set()
```

Stores the last `k` elements.

---

### Check Duplicate

```python
if nums[i] in window:
    return True
```

If already present, duplicate found within distance `k`.

---

### Add Current Element

```python
window.add(nums[i])
```

Insert current value into the sliding window.

---

### Maintain Window Size

```python
if len(window) > k:
    window.remove(nums[i-k])
```

Remove the element that moves out of the valid range.

This ensures we only keep the previous `k` elements.

---

### No Duplicate Found

```python
return False
```

After checking entire array.

---

## Complexity Analysis

### Time Complexity

```python
O(n)
```

Each element:

- Added once
- Removed once

Hash set operations:

```python
O(1)
```

Average case.

---

### Space Complexity

```python
O(k)
```

The set stores at most `k` elements.

---

## Pattern Learned

### Sliding Window + Hash Set

Use when:

- Need duplicates within a limited range.
- Need uniqueness inside a window.
- Need membership checks in O(1).

Common Problems:

1. Contains Duplicate II
2. Longest Substring Without Repeating Characters
3. Permutation in String
4. Find All Anagrams in a String
5. Subarray with Distinct Elements

---

## Revision Notes

- Only previous `k` elements matter.
- Use a Hash Set as the window.
- If current element already exists in window → return `True`.
- Add current element.
- Remove element that goes outside range `k`.
- Sliding Window + Hash Set pattern.
- Time Complexity: **O(n)**
- Space Complexity: **O(k)**

### Core Logic

```python
if nums[i] in window:
    return True

window.add(nums[i])

if len(window) > k:
    window.remove(nums[i-k])
```

Remember:

> Keep only the last `k` elements in the set. If a duplicate appears inside this window, the answer is True.
