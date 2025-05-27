class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m = len(rooms)
        n = len(rooms[0])
        INF = 2147483647
        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] != 0 and rooms[nr][nc] != -1 and ((nr, nc) not in visited or rooms[nr][nc] > (rooms[row][col] + 1)):
                    rooms[nr][nc] = rooms[row][col] + 1 if rooms[nr][nc] == INF else min(rooms[nr][nc], rooms[row][col] + 1)
                    q.append((nr, nc))
                    print(f"({nr}, {nc}) appended with cost = {rooms[nr][nc]}")
                    visited.add((nr, nc))
        