class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        def dfs(index, target):
            if index == 0:
                if target % coins[0] == 0:
                    return 1
                else:
                    return 0
            
            if dp[index][target] != -1:
                return dp[index][target]
            
            not_take = dfs(index - 1, target)
            take = 0
            if coins[index] <= target:
                take = dfs(index, target - coins[index])
            
            dp[index][target] = take + not_take
            return dp[index][target]
        
        return dfs(len(coins) - 1, amount)