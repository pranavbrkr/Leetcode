class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time, fresh = 0, 0
        rotten = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        while rotten and fresh:
            rotten_len = len(rotten)
            for _ in range(rotten_len):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr not in range(m) or nc not in range(n) or grid[nr][nc] != 1:
                        continue
                    rotten.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            time += 1
        
        return -1 if fresh else time