class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1] * n for _ in range(n)]

        def dfs(i, j):
            # no triangle if fewer than 2 vertices
            if j - i < 2:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            best = float('inf')
            for k in range(i + 1, j):
                cost = values[i] * values[k] * values[j] + dfs(i, k) + dfs(k, j)
                best = min(best, cost)

            dp[i][j] = best
            return best
        
        return dfs(0, n - 1)