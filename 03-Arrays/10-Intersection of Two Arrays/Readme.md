# Intersection of Two Arrays

## 📌 Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**.

- Each element in the result must be **unique**.
- The result can be returned in **any order**.

---

## 📝 Example

### Example 1

**Input**

```text
nums1 = [1,2,2,1]
nums2 = [2,2]
```

**Output**

```text
[2]
```

---

### Example 2

**Input**

```text
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
```

**Output**

```text
[9,4]
```

or

```text
[4,9]
```

Both are correct.

---

# 💡 Approach

The optimal solution uses **HashSet**.

### Steps

1. Convert the first array into a set.
2. Create an empty list for the answer.
3. Convert the second array into a set to remove duplicates.
4. Traverse the second set.
5. If an element exists in the first set, add it to the answer.
6. Return the answer.

Since searching inside a set takes **O(1)** time, the overall solution becomes very efficient.

---

# 🧠 Algorithm

1. Create a set from `nums1`.
2. Initialize an empty result list.
3. Iterate through `set(nums2)`.
4. Check whether the element exists in the first set.
5. If yes, append it.
6. Return the result.

---

# ✅ Python Solution

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = set(nums1)
        result = []

        for num in set(nums2):
            if num in set1:
                result.append(num)

        return result
```

---

# 🧪 Dry Run

Input

```text
nums1 = [1,2,2,1]
nums2 = [2,2]
```

Create set

```text
set1 = {1,2}
```

Unique elements of nums2

```text
{2}
```

Check

```
2 in set1 ✅
```

Append

```text
result = [2]
```

Return

```text
[2]
```

---

# ⏱️ Complexity Analysis

### Time Complexity

```
O(n + m)
```

- Creating first set → O(n)
- Creating second set → O(m)
- Traversing second set → O(m)

Overall:

```
O(n + m)
```

---

### Space Complexity

```
O(n + m)
```

For storing the two sets.

---

# 🔑 Key Concepts

- Arrays
- HashSet
- Set Operations
- Membership Lookup
- Removing Duplicates
- Efficient Searching

---

# 📚 What I Learned

- Using **set()** automatically removes duplicate values.
- HashSets provide **O(1)** average lookup time.
- Set-based solutions are much faster than nested loops.
- Efficiently solving array intersection problems using hashing.

---

**LeetCode:** 349. Intersection of Two Arrays

**Difficulty:** Easy

**Language:** Python
