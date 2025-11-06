from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Your code here
        result = []
        
        # for i in range(len(prices)-1):
        #     if prices[i] > prices[i+1]:
        #         continue
        #     else:
        #         profit = prices[i+1] - prices[i]
        #         result.append(profit)
        # return max(result)

        # to find max and min in a list
        # min_price = float('inf')
        # max_price = float('-inf')
        # max_profit = 0
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     if price > max_price:
        #         max_price = price
        # return max_price - min_price
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
            

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.maxProfit([7,1,5,3,6,4]))  # Expected: 5
    print(solution.maxProfit([7,6,4,3,1]))  # Expected: 0