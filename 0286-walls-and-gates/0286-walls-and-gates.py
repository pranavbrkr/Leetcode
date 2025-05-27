class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        visited = set()
        dist = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        def addRoom(row, col):
            if (row < 0 or row == m or col < 0 or col == n or (row, col) in visited or rooms[row][col] == -1):
                return
            q.append((row, col))
            visited.add((row, col))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1