class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        m = len(grid)
        n = len(grid[0])
        fresh = 0

        rotten = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while rotten and fresh:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if nr not in range(m) or nc not in range(n) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    rotten.append((nr, nc))
            time += 1
        
        return -1 if fresh else time