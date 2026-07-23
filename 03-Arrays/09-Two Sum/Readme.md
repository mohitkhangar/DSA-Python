# Two Sum

## 📌 Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

- Each input has exactly one solution.
- You may not use the same element twice.
- Return the answer in any order.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [2,7,11,15]
target = 9
```

**Output**

```text
[0,1]
```

**Explanation**

```
nums[0] + nums[1] = 2 + 7 = 9
```

---

### Example 2

**Input**

```text
nums = [3,2,4]
target = 6
```

**Output**

```text
[1,2]
```

---

### Example 3

**Input**

```text
nums = [3,3]
target = 6
```

**Output**

```text
[0,1]
```

---

# 💡 Approach

A brute-force solution checks every pair of numbers, resulting in **O(n²)** time complexity.

A more efficient approach uses a **HashMap (Dictionary)**.

The idea is:

1. Create an empty dictionary.
2. Traverse the array once.
3. For every number:
   - Calculate its complement.
   - Check whether the complement already exists in the dictionary.
   - If yes, return both indices.
   - Otherwise, store the current number and its index.
4. Continue until the pair is found.

This allows finding the answer in a single traversal.

---

# 🧠 Algorithm

1. Initialize an empty HashMap.
2. Traverse the array.
3. Compute:

```python
complement = target - current_number
```

4. If the complement exists in the HashMap:
   - Return its index and the current index.
5. Otherwise:
   - Store the current number with its index.
6. Repeat until the answer is found.

---

# ✅ Python Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
```

---

# ⏱️ Complexity Analysis

### Time Complexity

```
O(n)
```

Only one traversal of the array is required.

### Space Complexity

```
O(n)
```

The HashMap stores at most all elements.

---

# 🔑 Key Concepts

- Arrays
- HashMap (Dictionary)
- One-pass traversal
- Complement technique
- Optimal lookup using hashing
- Time optimization

---

# 📚 What I Learned

- How HashMaps reduce lookup time from **O(n)** to **O(1)**.
- Solving the Two Sum problem in a single pass.
- Using complements to efficiently find matching pairs.
- Improving brute-force solutions using hashing.
- Understanding time-space trade-offs in algorithm design.

---

**LeetCode:** 1. Two Sum  
**Difficulty:** Easy  
**Language:** Python
