class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        nums.insert(0, 1)

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i > j:
                    continue
                max_coins = float('-inf')
                for index in range(i, j + 1):
                    cost = nums[i - 1] * nums[index] * nums[j + 1] + dp[i][index - 1] + dp[index + 1][j]
                    max_coins = max(max_coins, cost)
                dp[i][j] = max_coins
        
        return dp[1][n]