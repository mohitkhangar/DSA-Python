# Container With Most Water

## Problem Statement

Given an integer array `height`, where `height[i]` represents the height of a vertical line, find two lines that form a container that can hold the maximum amount of water.

Return the maximum amount of water the container can store.

---

## Example

### Input

```text
height = [1,8,6,2,5,4,8,3,7]
```

### Output

```text
49
```

### Explanation

The maximum area is formed by the lines with heights `8` and `7`.

```text
Width = 8 - 1 = 7
Height = min(8, 7) = 7

Area = Width × Height
     = 7 × 7
     = 49
```

---

## Core Idea

The area of the container depends on two things:

```text
Area = Width × Height
```

For two pointers `left` and `right`:

```text
Width = right - left
Height = min(height[left], height[right])
```

Therefore:

```text
Area = (right - left) × min(height[left], height[right])
```

The most important concept is:

> The shorter line determines the maximum height of the water.

---

## Approach: Two Pointers

We use two pointers:

- `left` starts from the beginning of the array.
- `right` starts from the end of the array.

```text
[1, 8, 6, 2, 5, 4, 8, 3, 7]
 ↑                               ↑
left                            right
```

At every step:

1. Calculate the width.
2. Find the shorter height.
3. Calculate the current area.
4. Update the maximum area.
5. Move the pointer pointing to the shorter line.

Continue until:

```text
left >= right
```

---

## Why Do We Move the Shorter Pointer?

This is the most important part of the problem.

Suppose:

```text
height[left] = 4
height[right] = 9
```

The water height is:

```text
min(4, 9) = 4
```

So the shorter line `4` is limiting the amount of water.

If we move the taller line `9`, the width becomes smaller, but the height is still limited by `4`.

Therefore, moving the taller line cannot improve the area with the current shorter line.

Instead, we move the shorter line.

There is a possibility that the next line is taller than `4`, which can increase the height enough to produce a larger area.

Therefore:

> Always move the pointer pointing to the shorter line.

---

## Algorithm

```text
1. Set left = 0.
2. Set right = len(height) - 1.
3. Set max_area = 0.

4. While left < right:

   a. Calculate width:
      width = right - left

   b. Calculate the shorter height:
      h = min(height[left], height[right])

   c. Calculate area:
      area = width × h

   d. Update maximum area:
      max_area = max(max_area, area)

   e. If height[left] < height[right]:
      move left forward

   f. Otherwise:
      move right backward

5. Return max_area.
```

---

## Python Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])

            area = width * h
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

## Code Explanation

### 1. Initialize Two Pointers

```python
left = 0
right = len(height) - 1
```

`left` starts at the first element.

`right` starts at the last element.

---

### 2. Initialize Maximum Area

```python
max_area = 0
```

This variable stores the largest area found so far.

---

### 3. Loop While Pointers Have Not Met

```python
while left < right:
```

A container requires two different lines, so we continue while `left` is smaller than `right`.

---

### 4. Calculate Width

```python
width = right - left
```

The distance between the two pointers is the width of the container.

---

### 5. Find the Limiting Height

```python
h = min(height[left], height[right])
```

The shorter line determines the maximum water height.

---

### 6. Calculate Area

```python
area = width * h
```

Formula:

```text
Area = Width × Height
```

---

### 7. Update Maximum Area

```python
max_area = max(max_area, area)
```

If the current area is larger than the previous maximum, update `max_area`.

---

### 8. Move the Shorter Pointer

```python
if height[left] < height[right]:
    left += 1
else:
    right -= 1
```

If the left line is shorter, move `left`.

Otherwise, move `right`.

This is the key step that makes the Two Pointer solution efficient.

---

## Dry Run

Given:

```text
height = [1,8,6,2,5,4,8,3,7]
```

### First Iteration

```text
left = 0
right = 8

height[left] = 1
height[right] = 7
```

Width:

```text
8 - 0 = 8
```

Height:

```text
min(1, 7) = 1
```

Area:

```text
8 × 1 = 8
```

Since `1 < 7`, move `left`.

---

### Second Iteration

```text
left = 1
right = 8

height[left] = 8
height[right] = 7
```

Width:

```text
8 - 1 = 7
```

Height:

```text
min(8, 7) = 7
```

Area:

```text
7 × 7 = 49
```

Update:

```text
max_area = 49
```

Since `8 > 7`, move `right`.

The process continues until the two pointers meet.

Final answer:

```text
49
```

---

## Brute Force vs Two Pointers

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Two Pointers | O(n) | O(1) |

### Brute Force

Check every possible pair of lines.

This takes:

```text
O(n²)
```

time.

### Two Pointers

Start from both ends and eliminate unnecessary comparisons.

This reduces the time complexity to:

```text
O(n)
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each pointer moves toward the other side at most once.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are used.

---

## Key Concepts

- Arrays
- Two Pointers
- Greedy Approach
- Maximum Tracking
- Space Optimization

---

## Two Pointer Pattern

A common structure for Two Pointer problems is:

```python
left = 0
right = len(nums) - 1

while left < right:
    # Process current pair

    if condition:
        left += 1
    else:
        right -= 1
```

The exact condition for moving the pointers depends on the problem.

---

## Common Mistakes

### 1. Using `max()` Instead of `min()`

Incorrect:

```python
h = max(height[left], height[right])
```

Correct:

```python
h = min(height[left], height[right])
```

The shorter line limits the water level.

---

### 2. Moving the Taller Pointer

The correct rule is:

```text
Move the shorter pointer.
```

---

### 3. Using the Wrong Width

Correct:

```python
width = right - left
```

---

### 4. Forgetting to Update the Maximum

Make sure to use:

```python
max_area = max(max_area, area)
```

Otherwise, the best area found so far will not be stored.

---

## Key Takeaway

> Start with two pointers at both ends, calculate `width × min(height[left], height[right])`, store the maximum area, and move the pointer pointing to the shorter line.

---

## Related Problems

- Two Sum II
- 3Sum
- 3Sum Closest
- Remove Duplicates from Sorted Array
- Move Zeroes
- Squares of a Sorted Array

---

## Problem Information

**LeetCode:** #11  
**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Greedy
