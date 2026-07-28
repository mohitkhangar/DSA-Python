# Majority Element

## Problem Statement

Given an integer array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than ⌊n / 2⌋ times**.

You may assume that the majority element always exists in the array.

---

## Example 1

### Input

```text
nums = [3,2,3]
```

### Output

```text
3
```

---

## Example 2

### Input

```text
nums = [2,2,1,1,1,2,2]
```

### Output

```text
2
```

---

## Approach (Boyer-Moore Voting Algorithm)

The Boyer-Moore Voting Algorithm works by maintaining:

- A **candidate** for the majority element.
- A **count** representing its current vote balance.

### Algorithm

1. Initialize `count = 0`.
2. Traverse the array.
3. If `count == 0`, choose the current element as the new candidate.
4. If the current element equals the candidate, increment the count.
5. Otherwise, decrement the count.
6. After traversal, the candidate is the majority element.

---

## Dry Run

Input

```text
[2,2,1,1,1,2,2]
```

| Element | Candidate | Count |
|---------:|----------:|------:|
|2|2|1|
|2|2|2|
|1|2|1|
|1|2|0|
|1|1|1|
|2|1|0|
|2|2|1|

Answer

```text
2
```

---

## Why Does It Work?

Every occurrence of a non-majority element cancels out one occurrence of the majority element.

Since the majority element appears **more than n/2 times**, it cannot be completely canceled, so it remains the final candidate.

---

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## Advantages

- Very efficient.
- Constant extra space.
- Single traversal.
- Best solution for this problem.

---

## Applications

- Election vote counting
- Data stream analysis
- Frequency-based algorithms
- Majority voting systems

---

## Python Solution

```python
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
```

---

## Output

```text
2
```

---

## Key Takeaways

- Uses the **Boyer-Moore Voting Algorithm**.
- Eliminates non-majority elements by vote cancellation.
- Requires only **one traversal**.
- Time Complexity: **O(n)**.
- Space Complexity: **O(1)**.
