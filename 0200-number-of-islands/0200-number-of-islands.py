class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        num_islands = 0

        def bfs(row, col):
            visited.add((row, col))
            q = collections.deque()
            q.append((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    r, c = qr + dr, qc + dc
                    if (r in range(m)) and (c in range(n)) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    num_islands += 1
        
        return num_islands