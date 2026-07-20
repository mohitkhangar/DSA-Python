# 🔍 Find Largest Element in Array

## 📌 Problem Statement

Given an array of integers, find and return the **largest element** present in the array.

---

## 🎯 Objective

- Learn how to traverse an array efficiently.
- Understand how to keep track of the maximum value.
- Improve problem-solving using iterative traversal.
- Build a strong foundation for more advanced array problems.

---

## 🧠 Approach

1. Assume the first element is the largest.
2. Traverse the array from the second element.
3. Compare each element with the current largest.
4. If a larger element is found, update the largest.
5. Return the largest element after completing the traversal.

---

## 💻 Python Solution

```python
def largest_element(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


arr = [12, 45, 7, 89, 23]
print(largest_element(arr))
```

---

## ▶️ Example

### Input

```text
[12, 45, 7, 89, 23]
```

### Output

```text
89
```

---

## 📝 Dry Run

Initial Array

```text
[12, 45, 7, 89, 23]
```

Initial largest

```text
largest = 12
```

Compare each element:

| Current Element | Largest | Action |
|----------------:|---------:|--------|
| 12 | 12 | No change |
| 45 | 45 | Update largest |
| 7 | 45 | No change |
| 89 | 89 | Update largest |
| 23 | 89 | No change |

Final Answer

```text
89
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

---

## 🔑 Key Learning

- Arrays are traversed using loops.
- Maintaining a running maximum is a common interview technique.
- This problem introduces the concept of **linear traversal**.
- The same pattern is used in many advanced problems like:
  - Second Largest Element
  - Maximum Difference
  - Best Time to Buy and Sell Stock
  - Kadane's Algorithm

---

## 🚀 Interview Tip

A common mistake is initializing the maximum as **0**.

Instead, always initialize it with the **first element** of the array:

```python
largest = arr[0]
```

This ensures the solution works correctly even when the array contains **negative numbers**.

Example:

```text
[-8, -3, -10]
```

Correct Answer:

```text
-3
```

---

## 📚 Concepts Practiced

- Arrays
- Iteration
- Linear Search
- Maximum Tracking
- Time Complexity Analysis

---

⭐ This solution is part of my **DSA in Python** journey, where I solve and document important interview problems with clean code, detailed explanations, and complexity analysis.
