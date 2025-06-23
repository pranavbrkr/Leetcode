class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cache[i][j] = grid[0][0]
                    continue
                
                up = left = float('inf')
                if i > 0:
                    up = cache[i - 1][j]
                if j > 0:
                    left = cache[i][j - 1]
                
                cache[i][j] = grid[i][j] + min(up, left)
        
        print(cache)
        return cache[m - 1][n - 1]