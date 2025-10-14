class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [[grid[0][0], 0, 0]]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited.add((0, 0))

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr not in range(n) or nc not in range(n) or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heapq.heappush(heap, [max(t, grid[nr][nc]), nr, nc])