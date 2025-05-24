class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        m = len(grid)
        n = len(grid[0])

        def bfs(x, y):
            q = deque([(x, y)])
            area = 0

            while q:
                row, col = q.popleft()
                area += 1
                print(f"Area incremented to {area} at ({row}, {col})")
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    max_area = max(max_area, bfs(i, j))
        
        return max_area