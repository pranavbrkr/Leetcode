class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        islands = set()
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(row, col, base_r, base_c, islands_vec):
            visited.add((row, col))
            islands_vec.append((row - base_r, col - base_c))
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr in range(m) and nc in range(n) and (nr, nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr, nc, base_r, base_c, islands_vec)



        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    islands_vec = []
                    dfs(i, j, i, j, islands_vec)
                    islands.add(tuple(islands_vec))

        return len(islands)