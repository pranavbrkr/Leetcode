class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[1] = cost[0]

        for i in range(2, n + 1):
            print(i-1, i-2)
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])
        
        print(dp)
        return min(dp[n], dp[n - 1])