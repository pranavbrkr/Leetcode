class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]

        for index in range(n - 1, -1, -1):
            for buy in range(2):
                for rem in range(1, k + 1):
                    if buy:
                        dp[index][buy][rem] = max(
                            -prices[index] + dp[index + 1][0][rem],
                            0 + dp[index + 1][1][rem]
                        )
                    else:
                        dp[index][buy][rem] = max(
                            prices[index] + dp[index + 1][1][rem - 1],
                            0 + dp[index + 1][0][rem]
                        )
        
        return dp[0][1][k]