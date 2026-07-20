# 🚀 Move Zeroes

## 📌 Problem Statement

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The operation must be performed **in-place** without making a copy of the array.

**LeetCode:** 283 - Move Zeroes

---

## 💡 Examples

### Example 1

**Input**

```text
nums = [0,1,0,3,12]
```

**Output**

```text
[1,3,12,0,0]
```

---

### Example 2

**Input**

```text
nums = [0]
```

**Output**

```text
[0]
```

---

## 🧠 Approach

The optimal solution uses the **Two Pointer** technique.

- Pointer `i` traverses the array.
- Pointer `count` keeps track of the position where the next non-zero element should be placed.

Whenever a non-zero element is found:

1. Swap it with the element at index `count`.
2. Increment `count`.

This automatically pushes all zeroes toward the end while preserving the order of non-zero elements.

---

## 🔍 Algorithm

1. Initialize `count = 0`.
2. Traverse the array from left to right.
3. If the current element is non-zero:
   - Swap `nums[count]` and `nums[i]`.
   - Increment `count`.
4. Continue until the end of the array.
5. The array is now rearranged with all zeroes at the end.

---

## ✅ Python Solution

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
```

---

## 📊 Dry Run

### Input

```text
nums = [0,1,0,3,12]
```

| i | nums[i] | count | Action | Array |
|---|---------|-------|--------|-------|
|0|0|0|Skip|[0,1,0,3,12]|
|1|1|0|Swap(0,1)|[1,0,0,3,12]|
|2|0|1|Skip|[1,0,0,3,12]|
|3|3|1|Swap(1,3)|[1,3,0,0,12]|
|4|12|2|Swap(2,4)|[1,3,12,0,0]|

Final Answer:

```text
[1,3,12,0,0]
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## 🔑 Key Concepts

- Arrays
- Two Pointers
- In-place Swapping
- Traversal

---

## 🎯 Learning Outcome

After solving this problem, you will understand:

- How the Two Pointer technique works.
- How to perform in-place array modification.
- How swapping preserves the relative order of non-zero elements.
- Why this approach achieves **O(n)** time and **O(1)** space.

---

⭐ Difficulty: **Easy**

🏷️ Tags: **Arrays, Two Pointers, In-place Algorithm**
