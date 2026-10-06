# 438. Find All Anagrams in a String

## Problem
Given two strings `s` and `p`, return all starting indices of `p`'s anagrams in `s`.

An anagram contains the same characters with the same frequencies, but the order may differ.

---

## Approach: Fixed Size Sliding Window + Frequency Counter

Since every anagram of `p` must have the same length as `p`, we maintain a sliding window of size `len(p)` over `s`.

We compare:

- Character frequency of `p`
- Character frequency of the current window

Whenever both frequency maps match, we found an anagram.

---

## Algorithm

1. Create a frequency map for `p`.
2. Initialize a sliding window over `s`.
3. Add the current character to the window frequency map.
4. If window size exceeds `len(p)`:
   - Remove the leftmost character.
   - Move the left pointer.
5. Compare window frequency with target frequency.
6. If equal, store the starting index.

---

## Python Solution

```python
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter()

        result = []
        left = 0

        for right in range(len(s)):
            window_count[s[right]] += 1

            if right - left + 1 > len(p):
                window_count[s[left]] -= 1

                if window_count[s[left]] == 0:
                    del window_count[s[left]]

                left += 1

            if window_count == p_count:
                result.append(left)

        return result
```

---

## Example

### Input

```python
s = "cbaebabacd"
p = "abc"
```

### Windows

| Window | Frequency Match | Index |
|----------|----------|----------|
| cba | ✅ | 0 |
| bae | ❌ | - |
| aeb | ❌ | - |
| eba | ❌ | - |
| bab | ❌ | - |
| aba | ❌ | - |
| bac | ✅ | 6 |

### Output

```python
[0, 6]
```

---

## Dry Run

Target Frequency:

```python
{
 'a':1,
 'b':1,
 'c':1
}
```

First window:

```python
"cba"
```

Window frequency:

```python
{
 'c':1,
 'b':1,
 'a':1
}
```

Matches target → add index `0`.

Continue sliding until another match is found at index `6`.

---

## Complexity Analysis

### Time Complexity

- Each character enters the window once.
- Each character leaves the window once.

**O(n)**

---

### Space Complexity

Frequency maps store at most 26 lowercase letters.

**O(1)**

---

## Pattern Recognition

This problem is a classic example of:

- Fixed Size Sliding Window
- Frequency Counting
- Anagram Detection

---

## Similar Problems

- 567. Permutation in String
- 76. Minimum Window Substring
- 3. Longest Substring Without Repeating Characters
- 424. Longest Repeating Character Replacement
- 904. Fruit Into Baskets

---

## Key Takeaway

Whenever you need to find:

- Anagrams
- Permutations
- Fixed-length substring matches

Think:

**Sliding Window + Frequency Map**
