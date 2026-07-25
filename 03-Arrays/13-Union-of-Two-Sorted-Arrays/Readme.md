# 🔗 Union of Two Sorted Arrays

## 📌 Problem Statement

Given two **sorted arrays**, return their **union**.

The union should:

- Contain all **distinct elements**
- Be sorted in ascending order

---

# 📝 Example

### Example 1

**Input**

```text
a = [1,2,3,4,5]
b = [1,2,3,6,7]
```

**Output**

```text
[1,2,3,4,5,6,7]
```

---

### Example 2

**Input**

```text
a = [1,1,2,3]
b = [2,2,4]
```

**Output**

```text
[1,2,3,4]
```

---

# 💡 Approach

Since both arrays are already sorted, we can efficiently merge them using the **Two Pointer Technique**.

### Steps

1. Initialize two pointers:
   - `i` for the first array.
   - `j` for the second array.

2. Compare elements:
   - If `a[i] <= b[j]`, process `a[i]`.
   - Otherwise, process `b[j]`.

3. Before inserting into the union array:
   - Check whether it is already the last inserted element.
   - This removes duplicates.

4. After one array finishes, add the remaining unique elements from the other array.

---

# 🐍 Python Solution

```python
class Solution:
    def findUnion(self, a, b):

        i = 0
        j = 0
        union = []

        while i < len(a) and j < len(b):

            if a[i] <= b[j]:

                if len(union) == 0 or union[-1] != a[i]:
                    union.append(a[i])

                i += 1

            else:

                if len(union) == 0 or union[-1] != b[j]:
                    union.append(b[j])

                j += 1

        while i < len(a):

            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])

            i += 1

        while j < len(b):

            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])

            j += 1

        return union
```

---

# 🔎 Dry Run

### Input

```text
a = [1,2,3]
b = [2,3,4]
```

| i | j | Compare | Union |
|---|---|---------|-------|
|0|0|1 ≤ 2|[1]|
|1|0|2 = 2|[1,2]|
|2|1|3 = 3|[1,2,3]|
|-|2|4 Remaining|[1,2,3,4]|

Final Answer

```text
[1,2,3,4]
```

---

# ⏱ Complexity Analysis

### Time Complexity

```
O(n + m)
```

- Traverse both arrays only once.

---

### Space Complexity

```
O(n + m)
```

- Stores the union of both arrays.

---

# 🎯 Key Concepts

- Arrays
- Two Pointer Technique
- Merging Sorted Arrays
- Duplicate Removal
- Linear Traversal

---

# 📚 Learning Outcome

After solving this problem, I learned:

- How to merge two sorted arrays efficiently.
- Using the Two Pointer Technique to avoid nested loops.
- Removing duplicates while traversing.
- Solving merge-based problems in linear time.

---

⭐ This problem is one of the most important Two Pointer interview questions and forms the foundation for problems involving merging sorted arrays.
