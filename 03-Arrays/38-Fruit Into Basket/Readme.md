# 904. Fruit Into Baskets

## Pattern
**Sliding Window + HashMap (At Most K Distinct Elements)**

---

## Key Observation

We have:

- 2 baskets
- Each basket can hold only 1 fruit type
- Need the longest contiguous subarray containing **at most 2 distinct fruit types**

This becomes:

> Find the longest subarray with at most 2 distinct elements.

---

## Approach

Use a sliding window:

- Expand window using `right`
- Store fruit frequencies in a hashmap
- If distinct fruit types become more than 2:
  - Shrink window from `left`
  - Remove frequencies
  - Delete fruit type when count becomes 0
- Track maximum valid window length

---

## Algorithm

1. Create a frequency map.
2. Initialize:
   - `left = 0`
   - `max_fruits = 0`
3. Traverse using `right`.
4. Add current fruit to hashmap.
5. While distinct fruits > 2:
   - Decrease count of left fruit.
   - Remove fruit type if frequency becomes 0.
   - Move left pointer.
6. Update answer using current window size.
7. Return maximum length.

---

## Code

```python
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)

        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
```

---

## Example

Input:

```python
fruits = [1,2,3,2,2]
```

Process:

```text
[1]           ✓
[1,2]         ✓
[1,2,3]       ✗ (3 types)

Shrink

[2,3]         ✓
[2,3,2]       ✓
[2,3,2,2]     ✓
```

Answer:

```python
4
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each element enters and leaves the window at most once.

### Space Complexity

```text
O(1)
```

HashMap stores at most 3 fruit types.

---

## Revision Notes

- Longest subarray with **at most 2 distinct elements**
- Use Sliding Window + Frequency Map
- Expand with `right`
- Shrink while `len(count) > 2`
- Window length:

```python
right - left + 1
```

### Pattern Template

```python
for right in range(len(nums)):
    add(nums[right])

    while invalid_window:
        remove(nums[left])
        left += 1

    answer = max(answer, right - left + 1)
```

### Similar Problems

- 3. Longest Substring Without Repeating Characters
- 424. Longest Repeating Character Replacement
- 1004. Max Consecutive Ones III
- 340. Longest Substring with At Most K Distinct Characters
- 159. Longest Substring with At Most Two Distinct Characters
