# Remove Duplicates from Sorted Array

## 📌 Problem

Given a sorted integer array `nums`, remove the duplicates **in-place** such that each unique element appears only once. Return the number of unique elements (`k`).

The first `k` elements of the array should contain the unique values in sorted order.

**LeetCode:** 26  
**Difficulty:** Easy

---

## 💡 Approach

This problem is solved using the **Two Pointer** technique.

- Pointer `i` keeps track of the position of the last unique element.
- Pointer `j` traverses the array from left to right.
- Whenever a new unique element is found, move it to the next available position.

This allows us to modify the array **in-place** without using any extra space.

---

## 📝 Algorithm

1. If the array is empty, return `0`.
2. Initialize pointer `i = 0`.
3. Traverse the array using pointer `j` from index `1`.
4. Compare `nums[i]` and `nums[j]`.
5. If they are different:
   - Increment `i`.
   - Copy `nums[j]` to `nums[i]`.
6. Return `i + 1`, which represents the number of unique elements.

---

## ✅ Python Solution

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

---

## 📊 Dry Run

### Input

```text
nums = [1,1,2,2,3]
```

| i | j | nums[i] | nums[j] | Action | Array |
|---|---|---------|---------|--------|-------|
|0|1|1|1|Duplicate → Skip|[1,1,2,2,3]|
|0|2|1|2|Unique → i++, copy|[1,2,2,2,3]|
|1|3|2|2|Duplicate → Skip|[1,2,2,2,3]|
|1|4|2|3|Unique → i++, copy|[1,2,3,2,3]|

Return:

```text
3
```

The first three elements are:

```text
[1,2,3]
```

---

## ⏱️ Time Complexity

- **O(n)**

The array is traversed only once.

---

## 💾 Space Complexity

- **O(1)**

No extra space is used.

---

## 🧠 Concepts Learned

- Arrays
- Two Pointers
- In-place Array Modification
- Linear Traversal
- Time & Space Optimization

---

## 🔖 Tags

`Array` `Two Pointers` `Easy`
