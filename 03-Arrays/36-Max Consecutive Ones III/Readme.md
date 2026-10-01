# 1004. Max Consecutive Ones III

## Problem Statement

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` zeros.

---

## Intuition

The problem says:

> You may flip at most `k` zeros into ones.

Instead of thinking about flipping, think differently:

A valid subarray is one that contains at most `k` zeros.

Why?

Because all those zeros can be flipped into ones.

So the problem becomes:

> Find the longest subarray containing at most `k` zeros.

This is a classic **Variable Size Sliding Window** problem. :chatgpt-content-reference{index="1"}

---

## Key Observation

We don't actually need to flip zeros.

We only need to count how many zeros exist inside our current window.

If:

```python
zero_count <= k
```

the window is valid.

If:

```python
zero_count > k
```

the window becomes invalid and must be shrunk from the left.

---

## Sliding Window Idea

Example:

```python
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

Initially:

```python
[1,1,1,0,0]
```

Zero count:

```python
2
```

Valid window.

Extend further:

```python
[1,1,1,0,0,0]
```

Zero count:

```python
3
```

Invalid because:

```python
3 > k
```

Move left pointer until:

```python
zero_count <= k
```

again.

Keep repeating.

The largest valid window length is the answer. :chatgpt-content-reference{index="2"}

---

## Algorithm

1. Initialize:
   - `left = 0`
   - `zero_count = 0`
   - `max_length = 0`

2. Expand window using `right`.

3. If current element is `0`:
   - Increment `zero_count`.

4. While:

```python
zero_count > k
```

Shrink window from left.

5. Update maximum window size.

6. Return maximum length.

---

## Dry Run

### Input

```python
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

---

### right = 0

```python
window = [1]
zero_count = 0
```

Length:

```python
1
```

---

### right = 1

```python
window = [1,1]
zero_count = 0
```

Length:

```python
2
```

---

### right = 3

```python
window = [1,1,1,0]
zero_count = 1
```

Valid.

---

### right = 4

```python
window = [1,1,1,0,0]
zero_count = 2
```

Still valid.

---

### right = 5

```python
window = [1,1,1,0,0,0]
zero_count = 3
```

Invalid.

Need shrinking.

Move left pointer until:

```python
zero_count <= 2
```

again.

---

Continue process.

Maximum valid window length becomes:

```python
6
```

Answer:

```python
6
```

---

## Code Explanation

### Initialize Variables

```python
left = 0
zero_count = 0
max_length = 0
```

- `left` → start of window
- `zero_count` → zeros inside window
- `max_length` → answer

---

### Expand Window

```python
for right in range(len(nums)):
```

Move right pointer through array.

---

### Count Zeros

```python
if nums[right] == 0:
    zero_count += 1
```

Track how many zeros are inside current window.

---

### Shrink Invalid Window

```python
while zero_count > k:
```

If too many zeros exist, remove elements from left.

---

### Remove Zero if Needed

```python
if nums[left] == 0:
    zero_count -= 1
```

When a zero leaves the window, reduce count.

---

### Move Left Pointer

```python
left += 1
```

Shrink window.

---

### Update Answer

```python
max_length = max(max_length, right - left + 1)
```

Store largest valid window length.

---

### Return Result

```python
return max_length
```

Longest valid window found.

---

## Why Sliding Window Works

The condition:

```python
zero_count <= k
```

defines whether a window is valid.

Whenever it becomes invalid:

```python
zero_count > k
```

we move the left pointer until it becomes valid again.

Each element:

- Enters window once
- Leaves window once

Therefore:

```python
O(n)
```

time complexity. :chatgpt-content-reference{index="3"}

---

## Complexity Analysis

### Time Complexity

```python
O(n)
```

Both pointers move at most `n` times. :chatgpt-content-reference{index="4"}

---

### Space Complexity

```python
O(1)
```

Only a few variables are used. :chatgpt-content-reference{index="5"}

---

## Pattern Learned

### Variable Size Sliding Window

Whenever you see:

- Longest subarray
- At most K changes
- At most K zeros
- At most K distinct elements

Think:

```python
Sliding Window
```

---

## Similar Problems

1. Longest Repeating Character Replacement (424)
2. Max Consecutive Ones II (487)
3. Fruit Into Baskets (904)
4. Longest Substring with At Most K Distinct Characters
5. Maximize the Confusion of an Exam (2024)

---

## Revision Notes

- Convert problem into:
  
```python
Longest subarray with at most k zeros
```

- Use Sliding Window.
- Count zeros in current window.
- If zeros exceed `k`, shrink window.
- Track maximum valid window length.
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

### Core Logic

```python
if nums[right] == 0:
    zero_count += 1

while zero_count > k:
    if nums[left] == 0:
        zero_count -= 1
    left += 1

max_length = max(max_length, right - left + 1)
```

### Interview One-Liner

> Find the longest window containing at most `k` zeros using a variable-size sliding window.
