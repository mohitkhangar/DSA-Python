# 121. Best Time to Buy and Sell Stock

🔗 LeetCode: 121. Best Time to Buy and Sell Stock  
🟢 Difficulty: Easy  
🏷️ Pattern: Sliding Window / Two Pointers / Running Minimum

---

## Problem Statement

You are given an array `prices` where `prices[i]` is the stock price on day `i`.

You want to maximize your profit by:

1. Buying one stock on a day.
2. Selling it on a future day.

Return the maximum profit possible. If no profit can be made, return `0`.

---

## Example

### Input

```text
prices = [7,1,5,3,6,4]
```

### Output

```text
5
```

### Explanation

```text
Buy at 1
Sell at 6

Profit = 6 - 1 = 5
```

---

## Intuition

To maximize profit:

```text
Profit = Selling Price - Buying Price
```

For every day, we want:

- The lowest price seen so far (best buying day)
- The current price as a potential selling day

Instead of checking all pairs:

```text
O(n²)
```

we keep track of the minimum price encountered.

---

## Key Observation

While scanning the array:

```text
If current price < minimum price
    Update minimum price

Else
    Calculate profit
    Update maximum profit
```

At every position we ask:

```text
What is the best profit if I sell today?
```

---

## Visualization

```text
prices = [7,1,5,3,6,4]
```

### Day 1

```text
Price = 7

min_price = 7
profit = 0
```

---

### Day 2

```text
Price = 1

min_price = 1
```

Better buying opportunity found.

---

### Day 3

```text
Price = 5

Profit = 5 - 1 = 4

max_profit = 4
```

---

### Day 4

```text
Price = 3

Profit = 3 - 1 = 2
```

No improvement.

---

### Day 5

```text
Price = 6

Profit = 6 - 1 = 5

max_profit = 5
```

Best profit so far.

---

### Day 6

```text
Price = 4

Profit = 4 - 1 = 3
```

No improvement.

---

Final Answer:

```text
5
```

---

## Optimal Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for price in prices:

            min_price = min(min_price, price)

            profit = price - min_price

            max_profit = max(max_profit, profit)

        return max_profit
```

---

## Step-by-Step Explanation

### Track minimum price

```python
min_price = min(min_price, price)
```

Stores the cheapest stock price seen so far.

---

### Calculate profit

```python
profit = price - min_price
```

Profit if we sell today.

---

### Update answer

```python
max_profit = max(max_profit, profit)
```

Keep the best profit seen.

---

## Why This Works

At every day:

```text
Current Price = Sell Price
Minimum Previous Price = Buy Price
```

Therefore:

```text
Profit = Sell - Buy
```

Since we always know the lowest price before today, we automatically evaluate the best possible transaction ending today.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Single pass through the array.

---

### Space Complexity

```text
O(1)
```

Only two variables are used.

---

# Pattern Recognition

Use this approach when:

- Need maximum profit/difference
- Buy before sell
- Find largest difference between two elements
- Order matters

Keywords:

- Maximum profit
- Buy then sell
- Future day
- Largest difference
- Stock prices

---

# Alternative Sliding Window View

Think of:

```text
left  = buy day
right = sell day
```

If:

```text
prices[right] < prices[left]
```

Move buy day:

```text
left = right
```

Otherwise:

```text
profit = prices[right] - prices[left]
```

Update maximum profit.

---

## Sliding Window Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):

            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right

            right += 1

        return max_profit
```

---

# Revision Notes

### Core Formula

```text
Profit = Selling Price - Buying Price
```

### Maintain

```text
Lowest buying price so far
Highest profit so far
```

### Pattern

```text
Running Minimum
+
Sliding Window
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

### Interview Takeaway

Whenever you see:

- Buy before sell
- Max profit
- Max difference
- Future element minus previous element

Think:

👉 Track the minimum value seen so far and compute the best profit in one pass.
