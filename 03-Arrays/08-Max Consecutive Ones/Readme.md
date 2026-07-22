# 🚀 Max Consecutive Ones

## 📌 Problem Statement

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

**LeetCode:** 485 - Max Consecutive Ones

---

## 💡 Examples

### Example 1

**Input**

```text
nums = [1,1,0,1,1,1]
```

**Output**

```text
3
```

---

### Example 2

**Input**

```text
nums = [1,0,1,1,0,1]
```

**Output**

```text
2
```

---

## 🧠 Approach

Traverse the array while maintaining:

- `count` → Current consecutive 1's.
- `max_count` → Maximum consecutive 1's seen so far.

- If the current element is `1`, increment `count` and update `max_count`.
- If the current element is `0`, reset `count` to `0`.

---

## 🔍 Algorithm

1. Initialize `count = 0` and `max_count = 0`.
2. Traverse the array.
3. If the current element is `1`:
   - Increment `count`.
   - Update `max_count`.
4. Otherwise, reset `count` to `0`.
5. Return `max_count`.

---

## ✅ Python Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        max_count = 0

        for num in nums:

            if num == 1:
                count += 1
                max_count = max(max_count, count)

            else:
                count = 0

        return max_count
```

---

## 📊 Dry Run

### Input

```text
nums = [1,1,0,1,1,1]
```

| Current Number | Count | Max Count |
|---------------:|------:|----------:|
|1|1|1|
|1|2|2|
|0|0|2|
|1|1|2|
|1|2|2|
|1|3|3|

Final Answer

```text
3
```

---

## 📈 Visual Representation

```text
1  1  0  1  1  1
│  │     │  │  │
└──┘     └─────┘

Maximum Consecutive Ones = 3
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
- Traversal
- Counting
- Sliding Count
- Linear Scan

---

## 🎯 Learning Outcome

After solving this problem, you will understand:

- How to count consecutive elements in an array.
- How to track the maximum value during traversal.
- How to solve array problems using a single pass.
- Why this solution achieves **O(n)** time and **O(1)** space.

---

⭐ **Difficulty:** Easy

🏷️ **Tags:** Arrays, Traversal, Counting
