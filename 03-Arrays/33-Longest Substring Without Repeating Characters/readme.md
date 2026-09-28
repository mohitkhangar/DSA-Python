# 3. Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

A substring is a continuous sequence of characters within a string.

---

## Example 1

```text
Input: s = "abcabcbb"
Output: 3

Explanation:
The longest substring without repeating characters is "abc".
```

---

## Example 2

```text
Input: s = "bbbbb"
Output: 1

Explanation:
The longest substring without repeating characters is "b".
```

---

## Example 3

```text
Input: s = "pwwkew"
Output: 3

Explanation:
The longest substring without repeating characters is "wke".
```

---

# Intuition

The main challenge is to maintain a substring that contains only unique characters.

Whenever we encounter a duplicate character, we must shrink the current substring until the duplicate is removed.

This is a perfect use case for the **Sliding Window Technique**.

We use:

- `left` → start of the current window
- `right` → end of the current window
- `set` → stores unique characters currently inside the window

The window always represents a valid substring with no repeated characters.

---

# Approach (Sliding Window)

1. Initialize:
   - `left = 0`
   - `longest = 0`
   - empty set

2. Move the `right` pointer through the string.

3. If the current character already exists in the set:
   - Remove characters from the left side.
   - Keep removing until the duplicate disappears.

4. Add the current character to the set.

5. Calculate current window length.

6. Update the maximum length found so far.

7. Return the maximum length.

---

# Dry Run

### Input

```text
s = "abcabcbb"
```

### Step 1

```text
Window = "a"
Length = 1
```

### Step 2

```text
Window = "ab"
Length = 2
```

### Step 3

```text
Window = "abc"
Length = 3
```

### Step 4

Current character = `a`

```text
Window = "abca"
```

Duplicate found.

Remove first `a` from the left.

```text
Window = "bca"
```

Length remains:

```text
3
```

Continue the same process.

Final Answer:

```text
3
```

---

# Optimal Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        chars = set()

        for right in range(len(s)):

            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            longest = max(longest, right - left + 1)

        return longest
```

---

# Code Explanation

## Step 1: Initialize Variables

```python
left = 0
longest = 0
chars = set()
```

### Purpose

- `left` keeps track of the beginning of the window.
- `longest` stores the maximum substring length.
- `chars` stores unique characters inside the current window.

---

## Step 2: Traverse the String

```python
for right in range(len(s)):
```

Move the `right` pointer from left to right.

Each iteration expands the window.

---

## Step 3: Remove Duplicate Characters

```python
while s[right] in chars:
    chars.remove(s[left])
    left += 1
```

If the current character already exists inside the window:

Example:

```text
Window = "abca"
```

Current character:

```text
a
```

Duplicate found.

Remove characters from the left side:

```text
Remove first a
Window = "bca"
```

Now the window becomes valid again.

---

## Step 4: Add Current Character

```python
chars.add(s[right])
```

Insert the current character into the set.

Now the window again contains only unique characters.

---

## Step 5: Update Maximum Length

```python
longest = max(longest, right - left + 1)
```

Current window size:

```python
right - left + 1
```

Compare it with the previous best answer.

Store the larger value.

---

## Step 6: Return Answer

```python
return longest
```

Return the length of the longest valid substring.

---

# Why Sliding Window Works

At any moment:

```text
Window = s[left ... right]
```

The window always contains unique characters.

If a duplicate appears:

```text
Expand → Duplicate Found → Shrink → Unique Again
```

This guarantees that:

- Every character enters the window once.
- Every character leaves the window once.

Therefore the algorithm is very efficient.

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Each character:

- Added to the set once
- Removed from the set once

Total operations:

```text
2 × n
```

Simplified:

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

In the worst case:

```text
s = "abcdefg"
```

All characters are unique.

The set stores all characters.

Therefore:

```text
O(n)
```

---

# Sliding Window Pattern

This problem follows the common Sliding Window template:

```python
left = 0

for right in range(len(data)):

    while invalid_window:
        left += 1

    answer = max(answer, window_size)
```

---

# Key Interview Takeaways

✅ Classic Sliding Window problem

✅ Uses Two Pointers (`left`, `right`)

✅ Uses Hash Set for O(1) lookup

✅ Expand window using `right`

✅ Shrink window using `left`

✅ Maintain only unique characters

✅ Time Complexity = O(n)

✅ Space Complexity = O(n)

---

# Revision Notes

```text
1. Use Sliding Window.
2. Maintain unique characters in a set.
3. Expand with right pointer.
4. If duplicate appears:
      Remove from left until duplicate disappears.
5. Update maximum length.
6. Return answer.

Pattern:
Longest Substring Without Repeating Characters
→ Sliding Window + Hash Set
```

## Tags

- Sliding Window
- Two Pointers
- Hash Set
- String

## Difficulty

**Medium**
