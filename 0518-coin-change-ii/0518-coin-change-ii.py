class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        for i in range(amount + 1):
            dp[0][i] = 1 if (i % coins[0] == 0) else 0
        
        for i in range(1, len(coins)):
            for j in range(amount + 1):
                not_take = dp[i - 1][j]
                take = 0
                if coins[i] <= j:
                    take = dp[i][j - coins[i]]
                dp[i][j] = take + not_take
        
        return dp[len(coins) - 1][amount]