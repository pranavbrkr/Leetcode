class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for L in range(2, n):
            for i in range(0, n - L):
                j = i + L
                best = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + values[i] * values[k] * values[j] + dp[k][j]
                    best = min(cost, best)
                dp[i][j] = best
        
        return dp[0][n - 1]