from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Your code here
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

# Test
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # 5
print(solution.maxProfit([7,6,4,3,1]))    # 0