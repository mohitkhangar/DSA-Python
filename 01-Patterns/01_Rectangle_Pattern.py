"""
Pattern 1: Rectangle Pattern
Platform: Striver A2Z DSA Sheet

Time Complexity: O(n²)
Space Complexity: O(1)
"""
class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()
