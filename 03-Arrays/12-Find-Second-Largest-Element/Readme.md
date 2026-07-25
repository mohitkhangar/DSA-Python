# 🔍 Find Second Largest Element in an Array

## 📌 Problem Statement

Given an array of positive integers, find the **second largest element** in the array.

If the second largest element does not exist, return **-1**.

---

# 📝 Example

### Example 1

**Input**

```
arr = [12, 35, 1, 10, 34, 1]
```

**Output**

```
34
```

**Explanation**

- Largest element = 35
- Second Largest = 34

---

### Example 2

**Input**

```
arr = [10, 10, 10]
```

**Output**

```
-1
```

**Explanation**

All elements are the same, so there is no second largest element.

---

# 💡 Approach

We traverse the array only once while maintaining two variables:

- **largest** → stores the largest element found so far.
- **second_largest** → stores the second largest element.

For every element:

1. If the current element is greater than the largest:
   - Update second largest with the previous largest.
   - Update largest.

2. Otherwise, if it is:
   - smaller than the largest
   - greater than second largest

   then update second largest.

This allows us to find the answer in a **single traversal**.

---

# 🐍 Python Solution

```python
class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second_largest = -1

        for num in arr:

            if num > largest:
                second_largest = largest
                largest = num

            elif num > second_largest and num != largest:
                second_largest = num

        return second_largest
```

---

# 🔎 Dry Run

### Input

```
arr = [12, 35, 1, 10, 34]
```

| Current Number | Largest | Second Largest |
|----------------|---------|----------------|
|12|12|-1|
|35|35|12|
|1|35|12|
|10|35|12|
|34|35|34|

### Final Answer

```
34
```

---

# ⏱ Complexity Analysis

### Time Complexity

```
O(n)
```

Only one traversal of the array is required.

---

### Space Complexity

```
O(1)
```

Only two extra variables are used.

---

# 🎯 Key Concepts

- Array Traversal
- Single Pass Algorithm
- Variable Tracking
- Conditional Statements
- Time Optimization

---

# 📚 Learning Outcome

After solving this problem, you will understand:

- How to find the second largest element efficiently.
- How to maintain multiple variables during a single traversal.
- Difference between the largest and second largest element.
- Why a one-pass solution is better than sorting the array.

---

⭐ This problem is one of the most common interview questions and is frequently asked in coding interviews.
