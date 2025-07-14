class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        m = len(grid)
        n = len(grid[0])

        rotten = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while rotten:
            for i in range(len(rotten)):
                o_row, o_col = rotten.popleft()
                for dr, dc in directions:
                    nr = dr + o_row
                    nc = dc + o_col
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.append((nr, nc))
            time += 1
        

        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return time