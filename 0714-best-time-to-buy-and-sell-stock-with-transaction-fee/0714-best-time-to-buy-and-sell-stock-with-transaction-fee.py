class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]

        def recursion(index, buy):
            if index == n:
                return 0
            
            if dp[index][buy] != -1:
                return dp[index][buy]
            
            if buy:
                dp[index][buy] = max(
                    -prices[index] + recursion(index + 1, 0),
                    0 + recursion(index + 1, 1)
                )
            else:
                dp[index][buy] = max(
                    prices[index] - fee + recursion(index + 1, 1),
                    0 + recursion(index + 1, 0)
                )
            
            return dp[index][buy]
        
        return recursion(0, 1)