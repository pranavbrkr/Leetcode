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

        # def recursion(index, buy, rem):
        #     if index == len(prices):
        #         return 0
            
        #     if rem == 0:
        #         return 0
            
        #     if dp[index][buy][rem] != -1:
        #         return dp[index][buy][rem]
            
        #     if buy:
        #         dp[index][buy][rem] = max(
        #             -prices[index] + recursion(index + 1, 0, rem),
        #             0 + recursion(index + 1, 1, rem)
        #         )
        #     else:
        #         dp[index][buy][rem] = max(
        #             prices[index] + recursion(index + 1, 1, rem - 1),
        #             0 + recursion(index + 1, 0, rem)
        #         )
            
        #     return dp[index][buy][rem]
        
        # return recursion(0, 1, k)
