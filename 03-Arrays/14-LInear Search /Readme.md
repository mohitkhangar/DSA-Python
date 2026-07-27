# Linear Search

## Problem Statement

Given an array of elements and a target value, find the index of the target using the **Linear Search** algorithm.

If the element exists, return its index; otherwise return **-1**.

---

## Example

### Input

```text
Array = [12, 45, 7, 23, 56, 89, 34]

Target = 23
```

### Output

```text
Element found at index 3
```

---

## Approach

Linear Search scans the array **from left to right**.

1. Start from the first element.
2. Compare each element with the target.
3. If a match is found, return its index.
4. If the entire array is traversed without finding the target, return **-1**.

---

## Algorithm

```text
for each element in array

    if element == target

        return index

return -1
```

---

## Dry Run

Array

```text
[12, 45, 7, 23, 56]
```

Target

```text
23
```

| Index | Value | Match |
|------:|------:|------:|
| 0 | 12 | ❌ |
| 1 | 45 | ❌ |
| 2 | 7 | ❌ |
| 3 | 23 | ✅ |

Return

```text
3
```

---

## Complexity Analysis

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

---

### Space Complexity

```text
O(1)
```

No extra memory is used.

---

## Advantages

- Very easy to implement.
- Works on both sorted and unsorted arrays.
- No preprocessing required.

---

## Disadvantages

- Slow for large datasets.
- Checks elements one by one.
- Less efficient than Binary Search for sorted arrays.

---

## Applications

- Searching in small datasets.
- Unsorted arrays.
- Linked Lists.
- Simple lookup operations.

---

## Python Implementation

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

---

## Output

```text
Element found at index 3
```

---

## Key Takeaways

- Linear Search is the simplest searching algorithm.
- It works on **unsorted** data.
- Time Complexity is **O(n)**.
- Space Complexity is **O(1)**.
- It is suitable for small datasets but inefficient for large collections.
