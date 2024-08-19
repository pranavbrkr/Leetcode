# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        n = len(prices)
        cheapest = prices[0]

        for i in range(1, n):
            if prices[i] < cheapest:
                cheapest = prices[i]
            else:
                if (prices[i] - cheapest) > max_profit:
                    max_profit = prices[i] - cheapest
        
        return max_profit