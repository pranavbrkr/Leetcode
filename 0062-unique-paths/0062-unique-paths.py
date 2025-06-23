class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [[-1] * n for _ in range(m)]
        cache[0][0] = 1
        def recursion(i, j):
            if i == 0 and j == 0:
                return cache[i][j]
            
            if i < 0 or j < 0:
                return 0

            if cache[i][j] != -1:
                return cache[i][j]
            
            up = recursion(i - 1, j)
            down = recursion(i, j - 1)

            cache[i][j] = up + down
            return cache[i][j]
        
        return recursion(m - 1, n - 1)