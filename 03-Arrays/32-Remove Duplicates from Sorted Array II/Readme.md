# 80. Remove Duplicates from Sorted Array II

## Problem

Given a sorted integer array `nums`, remove some duplicates **in-place** such that each unique element appears **at most twice**.

The relative order of the elements should remain the same.

Return `k`, where the first `k` elements contain the final valid array.

---

## Example

### Input

```text
nums = [1,1,1,2,2,3]
```

### Output

```text
k = 5
nums = [1,1,2,2,3,_]
```

Explanation:

- `1` appears 3 times → keep only 2.
- `2` appears 2 times → keep both.
- `3` appears once → keep it.

Final array:

```text
[1,1,2,2,3]
```

---

## Intuition

Since the array is already sorted:

```text
Duplicates are always adjacent.
```

We can use a pointer to build the valid array while scanning through the elements.

The key observation:

```text
Each number can appear at most 2 times.
```

So when processing a new number, we only need to compare it with the element that is **2 positions before** the current insertion position.

---

## Approach (Two Pointers)

### Pointer Meaning

- `i` → position where the next valid element should be placed.
- `num` → current element being processed.

Initially:

```python
i = 2
```

Why?

Because the first two elements are always valid.

Example:

```text
[1,1,1,2,2,3]
 ↑ ↑
 Keep first two elements
```

---

### Core Logic

For every element starting from index 2:

```python
if num != nums[i - 2]:
```

Then place it:

```python
nums[i] = num
i += 1
```

---

## Why Compare With `nums[i-2]`?

Suppose:

```text
Current Valid Array

[1,1]
```

Now another `1` arrives.

```text
num = 1
nums[i-2] = 1
```

Since they are equal:

```text
1 == 1
```

Adding this element would create:

```text
[1,1,1]
```

which is not allowed.

So we skip it.

---

### Example

Input:

```text
[1,1,1,2,2,3]
```

Start:

```text
i = 2
```

Current valid part:

```text
[1,1]
```

---

#### Process third 1

```text
num = 1
nums[i-2] = nums[0] = 1
```

Equal.

Skip.

---

#### Process 2

```text
num = 2
nums[i-2] = nums[0] = 1
```

Different.

Keep it.

```text
[1,1,2]
```

```text
i = 3
```

---

#### Process next 2

```text
num = 2
nums[i-2] = nums[1] = 1
```

Different.

Keep it.

```text
[1,1,2,2]
```

```text
i = 4
```

---

#### Process 3

```text
num = 3
nums[i-2] = nums[2] = 2
```

Different.

Keep it.

```text
[1,1,2,2,3]
```

```text
i = 5
```

Return:

```text
5
```

---

## Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)

        i = 2

        for num in nums[2:]:

            if num != nums[i - 2]:
                nums[i] = num
                i += 1

        return i
```

---

## Dry Run

Input:

```text
nums = [1,1,1,2,2,3]
```

### Initial

```text
i = 2
```

Valid array:

```text
[1,1]
```

---

### num = 1

```text
1 == nums[0]
```

Skip.

---

### num = 2

```text
2 != nums[0]
```

Keep.

```text
[1,1,2]
```

i = 3

---

### num = 2

```text
2 != nums[1]
```

Keep.

```text
[1,1,2,2]
```

i = 4

---

### num = 3

```text
3 != nums[2]
```

Keep.

```text
[1,1,2,2,3]
```

i = 5

---

## Why This Works

Because the array is sorted:

```text
All duplicates are consecutive.
```

By checking:

```python
nums[i - 2]
```

we guarantee that no element can appear more than twice.

If the current number equals the element two positions back:

```text
Already appeared twice.
```

So we skip it.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Single traversal of the array.

---

### Space Complexity

```text
O(1)
```

Only a pointer variable is used.

---

## Key Takeaway

For sorted arrays:

```text
Duplicates are adjacent.
```

To allow:

- At most 1 occurrence → compare with previous element.
- At most 2 occurrences → compare with element 2 positions back.
- At most k occurrences → compare with element k positions back.

This pattern is frequently used in sorted-array duplicate problems.
