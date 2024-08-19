# https://leetcode.com/problems/number-of-islands/

class Solution:

    visited = []

    def bfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or self.visited[i][j] or grid[i][j] == "0":
            return

        self.visited[i][j] = True
        self.bfs(grid, i + 1, j, m, n)
        self.bfs(grid, i, j + 1, m, n)
        self.bfs(grid, i - 1, j, m, n)
        self.bfs(grid, i, j - 1, m, n)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.visited = [[False for _ in range(n)] for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):
                if self.visited[i][j]:
                    continue
                if grid[i][j] == "1":
                    self.bfs(grid, i, j, m, n)
                    count += 1

        return count