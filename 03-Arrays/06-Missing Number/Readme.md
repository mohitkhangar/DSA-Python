# 🚀 Missing Number

## 📌 Problem Statement

Given an array `nums` containing `n` distinct numbers in the range **[0, n]**, return the **only number** in the range that is missing from the array.

**LeetCode:** 268 - Missing Number

---

## 💡 Examples

### Example 1

**Input**

```text
nums = [3,0,1]
```

**Output**

```text
2
```

---

### Example 2

**Input**

```text
nums = [0,1]
```

**Output**

```text
2
```

---

### Example 3

**Input**

```text
nums = [9,6,4,2,3,5,7,0,1]
```

**Output**

```text
8
```

---

## 🧠 Approach

The array contains numbers from **0** to **n**, with exactly one number missing.

1. Calculate the expected sum of numbers from **0** to **n** using the mathematical formula:

```text
Sum = n × (n + 1) / 2
```

2. Calculate the actual sum of all elements in the array.

3. The difference between the expected sum and the actual sum is the missing number.

---

## 🔍 Algorithm

1. Find the length of the array.
2. Compute the expected sum using:

```text
n × (n + 1) // 2
```

3. Compute the actual sum of the array.
4. Return:

```text
expected_sum - actual_sum
```

---

## ✅ Python Solution

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        expected_sum = n * (n + 1) // 2

        actual_sum = sum(nums)

        return expected_sum - actual_sum
```

---

## 📊 Dry Run

### Input

```text
nums = [3,0,1]
```

| Step | Value |
|------|-------|
| Length (n) | 3 |
| Expected Sum | 3 × (3+1) // 2 = 6 |
| Actual Sum | 3 + 0 + 1 = 4 |
| Missing Number | 6 - 4 = 2 |

Final Answer:

```text
2
```

---

## 📈 Visual Representation

```text
Expected Numbers

0   1   2   3
│   │   │   │

Expected Sum = 6

Actual Array

3   0   1

Actual Sum = 4

Missing Number

6 - 4 = 2
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

### Why Time Complexity is O(n)?

- Finding the length takes **O(1)**.
- Formula calculation takes **O(1)**.
- Calculating the array sum requires traversing all elements once, which takes **O(n)**.

Overall complexity:

```text
O(1) + O(1) + O(n) = O(n)
```

---

## 🔑 Key Concepts

- Arrays
- Mathematics
- Summation Formula
- Constant Space
- Linear Traversal

---

## 🎯 Learning Outcome

After solving this problem, you will understand:

- How mathematical formulas can optimize array problems.
- How to eliminate the need for extra space.
- How to compute the expected result without sorting.
- Why this solution runs in **O(n)** time and **O(1)** space.

---

## ⭐ Alternative Approach

Another optimal solution uses the **XOR** operation.

Both approaches have:

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

The mathematical approach is simpler and easier to understand, while the XOR approach is a common interview technique.

---

⭐ **Difficulty:** Easy

🏷️ **Tags:** Arrays, Mathematics, Bit Manipulation, Prefix Sum
