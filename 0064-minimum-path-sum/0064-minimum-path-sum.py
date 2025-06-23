class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [[-1] * n for _ in range(m)]

        def recursion(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            
            if i < 0 or j < 0:
                return float('inf')
            
            if cache[i][j] != -1:
                return cache[i][j]

            up = grid[i][j] + recursion(i - 1, j)
            left = grid[i][j] + recursion(i, j - 1)

            cache[i][j] = min(up, left)
            return cache[i][j]
        
        return recursion(len(grid) - 1, len(grid[0]) - 1)