class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cache[0][0] = 1
                    continue
                
                up, left = 0, 0
                if i > 0:
                    up = cache[i - 1][j]
                if j > 0:
                    left = cache[i][j - 1]
                
                cache[i][j] = up + left
        
        return cache[m - 1][n - 1]