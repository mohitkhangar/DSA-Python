# 75. Sort Colors

## Intuition

The array contains only three values:

- 0 (Red)
- 1 (White)
- 2 (Blue)

Instead of sorting normally, we can place each value directly in its correct region.

## Dutch National Flag Algorithm

Use three pointers:

- `low` → next position for 0
- `mid` → current element
- `high` → next position for 2

### Rules

1. If `nums[mid] == 0`
   - Swap with `low`
   - Increment `low` and `mid`

2. If `nums[mid] == 1`
   - Already in correct position
   - Increment `mid`

3. If `nums[mid] == 2`
   - Swap with `high`
   - Decrement `high`
   - Do NOT increment `mid`

## Complexity

- Time: O(n)
- Space: O(1)

## Key Observation

At any moment:

[0 ... low-1] => all 0s
[low ... mid-1] => all 1s
[mid ... high] => unsorted
[high+1 ... n-1] => all 2s

By maintaining these regions, the array gets sorted in one traversal.
