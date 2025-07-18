class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for index in range(n - 1, -1, -1):
            for buy in range(2):
                if buy:
                    dp[index][buy] = max(
                        -prices[index] + dp[index + 1][0],
                        0 + dp[index + 1][1]
                    )
                else:
                    dp[index][buy] = max(
                        prices[index] - fee + dp[index + 1][1],
                        0 + dp[index + 1][0]
                    )
        
        return dp[0][1]