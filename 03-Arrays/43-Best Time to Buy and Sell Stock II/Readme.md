# 122. Best Time to Buy and Sell Stock II

## Problem Statement

You are given an integer array `prices` where `prices[i]` is the stock price on day `i`.

You may:

- Buy and sell the stock multiple times.
- Hold at most one stock at a time.
- Buy and sell on the same day if needed.

Return the maximum profit you can achieve.

---

## Intuition

Unlike Stock I, we are allowed to make multiple transactions.

Instead of finding one best buy-sell pair, we can collect profit from every upward price movement.

Whenever:

```text
prices[i] > prices[i-1]
```

we add the difference to our profit.

This works because every increasing sequence can be broken into smaller profitable transactions without changing the total profit.

Example:

```text
1 → 5 → 8

Profit:
(5 - 1) + (8 - 5)
= 4 + 3
= 7

Same as:
8 - 1 = 7
```

Therefore, we simply add all positive differences.

---

## Approach (Greedy)

1. Initialize `profit = 0`.
2. Traverse the array from index `1`.
3. If the current price is greater than the previous price:
   - Add the difference to profit.
4. Return total profit.

---

## Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
```

---

## Dry Run

### Input

```python
prices = [7,1,5,3,6,4]
```

### Iteration

| Day Change | Profit Added | Total Profit |
|------------|-------------|--------------|
| 1 → 7 | 0 | 0 |
| 1 → 5 | +4 | 4 |
| 5 → 3 | 0 | 4 |
| 3 → 6 | +3 | 7 |
| 6 → 4 | 0 | 7 |

### Output

```text
7
```

---

## Why This Works

Every positive difference represents a profitable transaction.

Instead of waiting for the largest future sell price, we capture every gain immediately.

This guarantees the maximum possible profit because:

```text
(a → b → c)

Profit = (b-a) + (c-b)
        = c-a
```

No profit is lost by splitting transactions.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

We traverse the array once.

### Space Complexity

```text
O(1)
```

Only a single variable is used to store profit.

---

## Pattern Recognition

- Greedy Algorithm
- Array Traversal
- Profit Accumulation
- Stock Trading Problems

---

## Key Takeaway

For Stock II:

> Add every positive price increase.

```python
if prices[i] > prices[i-1]:
    profit += prices[i] - prices[i-1]
```

This simple greedy strategy yields the maximum profit in a single pass.
