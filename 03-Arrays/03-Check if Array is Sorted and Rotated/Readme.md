# 🔄 Check if Array is Sorted and Rotated

## 📌 Problem Statement

Given an integer array `nums`, determine whether the array was originally sorted in **non-decreasing order** and then rotated some number of times (including zero).

Return:

- `True` if the array is sorted and rotated.
- `False` otherwise.

> **LeetCode:** 1752 - Check if Array Is Sorted and Rotated

---

## 🎯 Objective

- Understand the concept of rotated sorted arrays.
- Learn how to detect order violations in an array.
- Practice circular traversal using modulo (`%`).
- Improve logical reasoning for array-based interview questions.

---

## 🧠 Approach

### Key Observation

A sorted array has **0 breaks** in order.

Example:

```text
[1, 2, 3, 4, 5]
```

Comparisons:

```text
1 < 2 ✅
2 < 3 ✅
3 < 4 ✅
4 < 5 ✅
```

---

A sorted and rotated array has **exactly one break**.

Example:

```text
[3, 4, 5, 1, 2]
```

Comparisons:

```text
3 < 4 ✅
4 < 5 ✅
5 > 1 ❌
1 < 2 ✅
2 < 3 ✅   (Circular Comparison)
```

Only one order violation exists.

If there are **more than one** violations, the array cannot be obtained by rotating a sorted array.

---

## 💻 Python Solution

```python
class Solution:
    def check(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

            if count > 1:
                return False

        return True
```

---

## ▶️ Example 1

### Input

```text
[3,4,5,1,2]
```

### Output

```text
True
```

---

## ▶️ Example 2

### Input

```text
[2,1,3,4]
```

### Output

```text
False
```

---

## 📝 Dry Run

### Input

```text
[3,4,5,1,2]
```

Comparisons

| Current | Next | Result |
|---------:|-----:|:------:|
| 3 | 4 | ✅ |
| 4 | 5 | ✅ |
| 5 | 1 | ❌ |
| 1 | 2 | ✅ |
| 2 | 3 | ✅ |

Number of breaks = **1**

Answer:

```text
True
```

---

### Another Example

Input

```text
[2,1,3,4]
```

Comparisons

| Current | Next | Result |
|---------:|-----:|:------:|
| 2 | 1 | ❌ |
| 1 | 3 | ✅ |
| 3 | 4 | ✅ |
| 4 | 2 | ❌ |

Number of breaks = **2**

Answer

```text
False
```

---

## 💡 Why Circular Comparison?

The last element must also be compared with the first element.

Instead of writing a separate condition, use:

```python
nums[(i + 1) % n]
```

When `i` is the last index,

```text
(i + 1) % n = 0
```

This automatically compares the last element with the first.

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

---

## 🔑 Key Learning

- Rotated sorted arrays have **at most one order violation**.
- `%` (modulo) enables circular traversal.
- Early exit improves efficiency.
- Counting violations is a useful interview pattern.

---

## 🚀 Interview Tip

Instead of trying every possible rotation, simply count how many times:

```python
nums[i] > nums[(i + 1) % n]
```

If the count is:

- **0** → Already sorted
- **1** → Sorted and rotated
- **More than 1** → Not possible

This leads to an optimal **O(n)** solution.

---

## 📚 Concepts Practiced

- Arrays
- Linear Traversal
- Circular Traversal
- Modulo Operator
- Pattern Recognition
- Time Complexity Analysis

---

⭐ This solution is part of my **DSA in Python** journey, where I solve and document important interview problems with clean code, detailed explanations, dry runs, and complexity analysis.
