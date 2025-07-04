class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        prev_dp = [0, 0]

        for index in range(n - 1, -1, -1):
            curr_dp = []
            for buy in range(2):
                if buy:
                    curr_dp.append(max(
                        -prices[index] + prev_dp[0],
                        0 + prev_dp[1]
                    ))
                else:
                    curr_dp.append(max(
                        prices[index] + prev_dp[1],
                        0 + prev_dp[0]
                    ))
            prev_dp = curr_dp
        
        return prev_dp[1]