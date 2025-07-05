class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        dp = [[[-1 for _ in range(k + 1)] for _ in range(2)] for _ in range(len(prices))]
        def recursion(index, buy, rem):
            if index == len(prices):
                return 0
            
            if rem == 0:
                return 0
            
            if dp[index][buy][rem] != -1:
                return dp[index][buy][rem]
            
            if buy:
                dp[index][buy][rem] = max(
                    -prices[index] + recursion(index + 1, 0, rem),
                    0 + recursion(index + 1, 1, rem)
                )
            else:
                dp[index][buy][rem] = max(
                    prices[index] + recursion(index + 1, 1, rem - 1),
                    0 + recursion(index + 1, 0, rem)
                )
            
            return dp[index][buy][rem]
        
        return recursion(0, 1, k)
