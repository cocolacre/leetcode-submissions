# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List

class Solution:
    """
    O(n^2) solution, that exceeds time limit.
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        profit = 0
        if len(prices) == 0:
            return 0
        for ind, left in enumerate(prices[:-1]):
            for right in prices[ind+1:]:
                profit = right - left
                if profit > max_profit and profit > 0:
                    max_profit = profit
        return max_profit

class Solution:
    """
    O(n) "sliding window" solution, which I had a seed of intuition for during the day,
    but could not manage to grow it, so I cheated and asked youtube for help.
    TODO: visualize this?
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        profit = 0
        min_price = prices[0]
        if len(prices) == 0:
            return 0
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
        
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))

prices = [7,6,4,3,1]
print(sol.maxProfit(prices))


