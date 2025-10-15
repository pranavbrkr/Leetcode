class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prev_value):
            if r not in range(rows) or c not in range(cols) or matrix[r][c] <= prev_value:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            result = 1
            result = max(result, 1 + dfs(r + 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r - 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r, c + 1, matrix[r][c]))
            result = max(result, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = result
            return result
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, -1)
        
        return max(dp.values())