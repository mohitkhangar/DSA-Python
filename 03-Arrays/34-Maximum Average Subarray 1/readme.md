# 643. Maximum Average Subarray I

## Problem Statement
Given an integer array `nums` consisting of `n` elements and an integer `k`, find a contiguous subarray of length exactly `k` that has the maximum average value and return that average.

---

## Intuition

A brute-force approach would calculate the sum of every subarray of size `k`.

For each starting position:
- Compute the sum of the next `k` elements.
- Calculate the average.
- Keep track of the maximum.

This would take **O(n × k)** time, which is inefficient for large arrays.

Since every subarray has the same size `k`, we can use a **Sliding Window**.

Instead of recalculating the sum every time:
- Add the new element entering the window.
- Remove the element leaving the window.
- Update the maximum sum.

This reduces the complexity to **O(n)**.

---

## Key Observation

If we already know the sum of a window:

```python
[1, 12, -5, -6]
```

and want the next window:

```python
[12, -5, -6, 50]
```

We do not need to calculate the sum again.

Just:

```python
new_sum = old_sum + incoming_element - outgoing_element
```

This is the core idea of Sliding Window.

---

## Algorithm

1. Calculate the sum of the first `k` elements.
2. Store it as both:
   - `window_sum`
   - `max_sum`
3. Move the window one step at a time.
4. For each move:
   - Add the new element entering the window.
   - Remove the element leaving the window.
   - Update `max_sum`.
5. Return:

```python
max_sum / k
```

---

## Dry Run

### Input

```python
nums = [1,12,-5,-6,50,3]
k = 4
```

### First Window

```python
[1,12,-5,-6]
```

Sum:

```python
2
```

```python
window_sum = 2
max_sum = 2
```

---

### Move Window

Remove:

```python
1
```

Add:

```python
50
```

New Window:

```python
[12,-5,-6,50]
```

New Sum:

```python
2 - 1 + 50 = 51
```

```python
max_sum = 51
```

---

### Move Window Again

Remove:

```python
12
```

Add:

```python
3
```

New Window:

```python
[-5,-6,50,3]
```

New Sum:

```python
51 - 12 + 3 = 42
```

```python
max_sum = 51
```

---

### Final Answer

```python
51 / 4 = 12.75
```

Output:

```python
12.75
```

---

## Code

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k
```

---

## Code Explanation

### Initialize First Window

```python
window_sum = sum(nums[:k])
```

Calculates the sum of the first `k` elements.

Example:

```python
nums = [1,12,-5,-6,50,3]
k = 4

window_sum = 1 + 12 - 5 - 6 = 2
```

---

### Store Initial Maximum

```python
max_sum = window_sum
```

Initially, the first window is the maximum window found.

---

### Slide the Window

```python
for i in range(k, len(nums)):
```

Start from index `k` because the first window is already processed.

---

### Add Incoming Element

```python
window_sum += nums[i]
```

Include the new element entering the window.

---

### Remove Outgoing Element

```python
window_sum -= nums[i - k]
```

Remove the element leaving the window.

This keeps the window size exactly `k`.

---

### Update Maximum Sum

```python
max_sum = max(max_sum, window_sum)
```

If the current window sum is larger, update the answer.

---

### Return Maximum Average

```python
return max_sum / k
```

Since:

```python
Average = Sum / Number of Elements
```

and every window has size `k`.

---

## Complexity Analysis

### Time Complexity

```python
O(n)
```

- First window sum → `O(k)`
- Sliding through array → `O(n)`
- Overall → `O(n)`

---

### Space Complexity

```python
O(1)
```

Only a few variables are used.

---

## Pattern Learned

### Sliding Window (Fixed Size)

Use Sliding Window when:

- Subarray size is fixed.
- Need maximum/minimum sum.
- Need maximum/minimum average.
- Need count/frequency within a fixed-length window.

Common problems:

1. Maximum Average Subarray I
2. Maximum Sum Subarray of Size K
3. Contains Duplicate II
4. Sliding Window Maximum
5. Permutation in String

---

## Revision Notes

- Window size is fixed (`k`).
- Compute first window once.
- Slide by:
  - Add incoming element.
  - Remove outgoing element.
- Track maximum sum.
- Return `max_sum / k`.
- Fixed-size Sliding Window pattern.
- Time: **O(n)**
- Space: **O(1)**
