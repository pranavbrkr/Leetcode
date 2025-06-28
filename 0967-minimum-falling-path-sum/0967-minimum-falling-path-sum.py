class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[-1] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, m):
            for j in range(n):
                up = dp[i - 1][j]
                left = dp[i - 1][j - 1] if j > 0 else float('inf')
                right = dp[i - 1][j + 1] if j < n - 1 else float('inf')
                
                dp[i][j] = matrix[i][j] + min(up, left, right)
        
        answer = float('inf')
        for j in range(n):
            answer = min(answer, dp[m - 1][j])
        
        return answer