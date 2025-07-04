class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        
        def recursion(index, buy):
            if index == len(prices):
                return 0
            
            if dp[index][buy] != -1:
                return dp[index][buy]

            if buy:
                profit = max(
                    -prices[index] + recursion(index + 1, 0),
                    0 + recursion(index + 1, 1)
                )
            else:
                profit = max(
                    prices[index] + recursion(index + 1, 1),
                    0 + recursion(index + 1, 0)
                )
            
            dp[index][buy] = profit
            return profit
        
        return recursion(0, True)