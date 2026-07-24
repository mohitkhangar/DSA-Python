# 🔴🟡🔵 Sort Colors (LeetCode 75)

## 📌 Problem Statement

Given an array `nums` containing only `0`, `1`, and `2`, sort the array **in-place** so that all `0`s come first, followed by all `1`s, and then all `2`s.

You **must not** use the library's built-in sort function.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [2,0,2,1,1,0]
```

**Output**

```text
[0,0,1,1,2,2]
```

---

### Example 2

**Input**

```text
nums = [2,0,1]
```

**Output**

```text
[0,1,2]
```

---

## 💡 Approach

This problem is solved using the **Dutch National Flag Algorithm**.

We maintain three pointers:

- **low** → Next position for `0`
- **mid** → Current element being processed
- **high** → Next position for `2`

### Cases

### Case 1

If `nums[mid] == 0`

- Swap with `low`
- Increment `low`
- Increment `mid`

---

### Case 2

If `nums[mid] == 1`

- Already in the correct position
- Increment `mid`

---

### Case 3

If `nums[mid] == 2`

- Swap with `high`
- Decrement `high`
- Do **not** increment `mid`

This ensures the swapped element is checked.

---

## ✅ Python Solution

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

## 🧠 Dry Run

Input

```text
[2,0,2,1,1,0]
```

After processing:

```text
[0,0,1,1,2,2]
```

The array is sorted in a **single traversal**.

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|--------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## 🔑 Key Concepts Learned

- Dutch National Flag Algorithm
- Three Pointer Technique
- In-place Sorting
- One-pass Traversal
- Constant Space Optimization

---

## 📚 Learning Outcome

Through this problem, I learned how to efficiently partition an array containing three distinct values using the Dutch National Flag Algorithm. This approach performs sorting in **O(n)** time with **O(1)** extra space, making it the optimal solution for this problem.
