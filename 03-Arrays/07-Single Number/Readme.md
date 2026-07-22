# 🚀 Single Number

## 📌 Problem Statement

Given a **non-empty** array of integers `nums`, every element appears **twice** except for one. Find that single number.

You must implement a solution with **O(n)** time complexity and **O(1)** extra space.

**LeetCode:** 136 - Single Number

---

## 💡 Examples

### Example 1

**Input**

```text
nums = [2,2,1]
```

**Output**

```text
1
```

---

### Example 2

**Input**

```text
nums = [4,1,2,1,2]
```

**Output**

```text
4
```

---

### Example 3

**Input**

```text
nums = [1]
```

**Output**

```text
1
```

---

## 🧠 Approach

The optimal solution uses the **XOR (^)** operator.

Properties of XOR:

```text
a ^ a = 0
```

```text
a ^ 0 = a
```

Since every duplicate number appears twice, each pair cancels out after XOR. The only remaining value is the number that appears once.

---

## 🔍 Algorithm

1. Initialize `result = 0`.
2. Traverse the array.
3. XOR each element with `result`.
4. Return `result`.

---

## ✅ Python Solution

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            result ^= num

        return result
```

---

## 📊 Dry Run

### Input

```text
nums = [2,2,1]
```

| Current Number | Operation | Result |
|---------------:|-----------|-------:|
|2|0 ^ 2|2|
|2|2 ^ 2|0|
|1|0 ^ 1|1|

Final Answer

```text
1
```

---

## 📈 Visual Representation

```text
nums

2   2   1

↓

0 ^ 2 = 2

↓

2 ^ 2 = 0

↓

0 ^ 1 = 1

↓

Answer = 1
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
- Bit Manipulation
- XOR Operator
- Constant Space
- Linear Traversal

---

## 🎯 Learning Outcome

After solving this problem, you will understand:

- How the XOR operator works.
- Why duplicate numbers cancel each other.
- How to solve problems using bit manipulation.
- How to achieve **O(n)** time and **O(1)** extra space.

---

⭐ **Difficulty:** Easy

🏷️ **Tags:** Arrays, Bit Manipulation, XOR
