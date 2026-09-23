# Trapping Rain Water

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, calculate how much water can be trapped after raining.

---

## Example 1

### Input

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

### Output

```text
6
```

### Explanation

The elevation map can trap a total of `6` units of rain water.

The water is trapped between taller bars.

For example, between a left boundary of height `2` and a right boundary of height `3`, smaller bars in between can hold water.

---

## Example 2

### Input

```text
height = [4,2,0,3,2,5]
```

### Output

```text
9
```

---

# Core Idea

For every position, the amount of water that can be trapped depends on the tallest bar on its left and the tallest bar on its right.

The water above a position is:

```text
Water = min(left_max, right_max) - height[i]
```

If the current bar is already taller than the limiting boundary, no water is trapped there.

The main challenge is calculating the left and right maximum heights efficiently.

---

# Approach: Two Pointers

We use two pointers:

```text
left = 0
right = len(height) - 1
```

We also maintain:

```text
left_max
right_max
```

These represent:

- `left_max` → tallest bar found from the left side
- `right_max` → tallest bar found from the right side

At every step, compare:

```text
height[left]
height[right]
```

If:

```text
height[left] <= height[right]
```

we process the left side.

Otherwise, we process the right side.

---

# Why Two Pointers Work

Suppose:

```text
height[left] <= height[right]
```

The right side has a boundary at least as tall as the current left bar.

Therefore, the amount of water on the left side can be determined using `left_max`.

Similarly, when:

```text
height[right] < height[left]
```

we can determine the trapped water on the right side using `right_max`.

This allows us to process the array from both directions without creating extra arrays.

---

# Water Calculation

For the left side:

```text
Water = left_max - height[left]
```

For the right side:

```text
Water = right_max - height[right]
```

But water is added only when the current bar is lower than the corresponding maximum boundary.

---

# Algorithm

```text
1. Set left = 0.
2. Set right = n - 1.
3. Set left_max = 0.
4. Set right_max = 0.
5. Set water = 0.

6. While left < right:

   If height[left] <= height[right]:

       If height[left] >= left_max:
           Update left_max.

       Otherwise:
           Add left_max - height[left] to water.

       Move left forward.

   Otherwise:

       If height[right] >= right_max:
           Update right_max.

       Otherwise:
           Add right_max - height[right] to water.

       Move right backward.

7. Return water.
```

---

# Python Solution

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
```

---

# Code Explanation

## 1. Initialize Two Pointers

```python
left = 0
right = len(height) - 1
```

`left` starts from the beginning.

`right` starts from the end.

---

## 2. Initialize Maximum Heights

```python
left_max = 0
right_max = 0
```

`left_max` stores the highest bar encountered from the left.

`right_max` stores the highest bar encountered from the right.

---

## 3. Initialize Water

```python
water = 0
```

This variable stores the total amount of trapped water.

---

## 4. Process While Pointers Have Not Crossed

```python
while left < right:
```

We continue processing until the two pointers meet.

---

## 5. Process the Left Side

```python
if height[left] <= height[right]:
```

If the left bar is smaller or equal to the right bar, we process the left position.

---

## 6. Update `left_max`

```python
if height[left] >= left_max:
    left_max = height[left]
```

If the current left bar is taller than the previous maximum, update `left_max`.

For example:

```text
left_max = 2
height[left] = 3
```

Then:

```text
left_max = 3
```

---

## 7. Calculate Trapped Water

If the current bar is lower than `left_max`:

```python
water += left_max - height[left]
```

For example:

```text
left_max = 5
height[left] = 2
```

Then:

```text
water = 5 - 2
      = 3
```

So `3` units of water can be trapped above that position.

---

## 8. Move Left Pointer

```python
left += 1
```

After processing the current position, move to the next position.

---

## 9. Process the Right Side

If:

```python
height[left] > height[right]
```

we process the right side.

```python
if height[right] >= right_max:
    right_max = height[right]
```

Otherwise:

```python
water += right_max - height[right]
```

Then:

```python
right -= 1
```

---

# Dry Run

Consider:

```text
height = [4,2,0,3,2,5]
```

The left boundary is `4` and the right boundary is `5`.

The smaller boundary controls the water level for the current side.

---

### Position 1

```text
height = 2
left_max = 4
```

Water:

```text
4 - 2 = 2
```

Total:

```text
water = 2
```

---

### Position 2

```text
height = 0
left_max = 4
```

Water:

```text
4 - 0 = 4
```

Total:

```text
water = 2 + 4
      = 6
```

---

### Position 3

```text
height = 3
left_max = 4
```

Water:

```text
4 - 3 = 1
```

Total:

```text
water = 7
```

---

### Position 4

```text
height = 2
left_max = 4
```

Water:

```text
4 - 2 = 2
```

Total:

```text
water = 9
```

Final answer:

```text
9
```

---

# Important Formula

The general formula for trapped water at position `i` is:

```text
Water[i] = min(max_left[i], max_right[i]) - height[i]
```

The Two Pointer approach avoids explicitly creating the `max_left` and `max_right` arrays.

Instead, it maintains:

```text
left_max
right_max
```

while traversing the array.

---

# Why Not Use Extra Arrays?

A common approach is to create:

```text
left_max[]
right_max[]
```

and calculate the water for every position.

That approach takes:

```text
Time:  O(n)
Space: O(n)
```

The Two Pointer approach only uses:

```text
left
right
left_max
right_max
water
```

Therefore:

```text
Space = O(1)
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Each element is processed at most once.

---

## Space Complexity

```text
O(1)
```

Only a constant number of variables are used.

---

# Brute Force vs Prefix Arrays vs Two Pointers

| Approach | Time | Space |
|---|---:|---:|
| Brute Force | O(n²) | O(1) |
| Prefix Max Arrays | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |

The Two Pointer approach achieves linear time while using constant extra space.

---

# Key Concepts

- Arrays
- Two Pointers
- Prefix Maximum Concept
- Left Maximum
- Right Maximum
- Greedy Processing
- Space Optimization

---

# Important Pattern

The important pattern in this problem is:

```text
Two Pointers + Running Maximum
```

Maintain:

```text
left_max
right_max
```

and process the side whose current height is smaller.

---

# Common Mistakes

### 1. Using the Current Height Directly

Incorrect:

```python
water += height[left] - height[right]
```

The amount of water depends on the maximum boundary, not simply the neighboring heights.

---

### 2. Forgetting the `min()` Concept

The theoretical formula is:

```text
Water = min(left_max, right_max) - height[i]
```

The smaller boundary limits the amount of water.

---

### 3. Adding Water When the Current Bar Is a New Maximum

If:

```python
height[left] >= left_max
```

there is no water at that position.

Instead, update:

```python
left_max = height[left]
```

---

### 4. Moving the Wrong Pointer

The Two Pointer decision is based on:

```python
if height[left] <= height[right]:
```

Process the side with the smaller current boundary.

---

# Key Takeaways

1. Water needs a left boundary and a right boundary.

2. The water level is limited by the shorter boundary.

3. For each position:

```text
Water = min(left_max, right_max) - height[i]
```

4. Two pointers allow us to calculate the answer without storing extra arrays.

5. Maintain `left_max` and `right_max` while moving inward.

6. The final solution runs in:

```text
O(n) time
O(1) space
```

---

# One-Line Revision

> Move two pointers inward, maintain the maximum height from both sides, and add the difference between the current height and the limiting maximum whenever water can be trapped.

---

## Problem Information

**LeetCode:** #42  
**Difficulty:** Hard  
**Topics:** Array, Two Pointers, Dynamic Programming, Stack, Prefix/Suffix
