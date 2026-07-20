# ✅ Check if Array is Sorted

## 📌 Problem Statement

Given an array of integers, determine whether the array is sorted in **non-decreasing order**.

Return:

- `True` if the array is sorted.
- `False` otherwise.

---

## 🎯 Objective

- Understand how to verify sorted order in an array.
- Learn linear traversal of arrays.
- Practice adjacent element comparison.
- Build a foundation for problems involving sorted arrays.

---

## 🧠 Approach

1. Traverse the array from the second element.
2. Compare each element with its previous element.
3. If the current element is smaller than the previous one, the array is **not sorted**.
4. Return `False` immediately.
5. If the loop finishes without finding any violation, return `True`.

---

## 💻 Python Solution

```python
def is_sorted(arr):
    n = len(arr)

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False

    return True


arr = [1, 2, 3, 4, 5]

print(is_sorted(arr))
```

---

## ▶️ Example 1

### Input

```text
[1, 2, 3, 4, 5]
```

### Output

```text
True
```

---

## ▶️ Example 2

### Input

```text
[1, 3, 2, 4, 5]
```

### Output

```text
False
```

---

## 📝 Dry Run

Array

```text
[2, 5, 7, 9, 11]
```

Comparisons

| Previous | Current | Sorted? |
|----------:|--------:|:-------:|
| 2 | 5 | ✅ |
| 5 | 7 | ✅ |
| 7 | 9 | ✅ |
| 9 | 11 | ✅ |

No violation found.

Answer

```text
True
```

---

### Dry Run 2

Array

```text
[2, 5, 9, 4, 11]
```

Comparisons

| Previous | Current | Result |
|----------:|--------:|:------:|
| 2 | 5 | ✅ |
| 5 | 9 | ✅ |
| 9 | 4 | ❌ |

Since

```text
4 < 9
```

the array is **not sorted**.

Return

```text
False
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

---

## 🔑 Key Learning

- Compare **adjacent elements**.
- Exit early when an unsorted pair is found.
- Linear traversal is sufficient.
- This pattern is frequently used in array and binary search problems.

---

## 🚀 Interview Tip

Instead of checking every possible pair, only compare **adjacent elements**.

If every adjacent pair satisfies

```text
arr[i] >= arr[i-1]
```

then the entire array is sorted.

---

## 📚 Concepts Practiced

- Arrays
- Linear Traversal
- Adjacent Comparison
- Early Return
- Time Complexity Analysis

---

⭐ This solution is part of my **DSA in Python** journey, where I solve and document important interview problems with clean code, detailed explanations, and complexity analysis.
