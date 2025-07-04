class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        def recursion(index, buy, cap):
            if cap == 0:
                return 0
            if index == n:
                return 0
            
            if dp[index][buy][cap] != -1:
                return dp[index][buy][cap]
            
            if buy:
                dp[index][buy][cap] = max(
                    -prices[index] + recursion(index + 1, 0, cap),
                    0 + recursion(index + 1, 1, cap),
                )
            else:
                dp[index][buy][cap] = max(
                    prices[index] + recursion(index + 1, 1, cap - 1),
                    0 + recursion(index + 1, 0, cap),
                )
            
            return dp[index][buy][cap]
        
        return recursion(0, 1, 2)