class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def countNeighbors(r, c):
            num_neighbors = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or j < 0 or i == rows or j == cols:
                        continue
                    if board[i][j] in [1, 3]:
                        num_neighbors += 1
            return num_neighbors
        
        for i in range(rows):
            for j in range(cols):
                neighbors = countNeighbors(i, j)
                if board[i][j]:
                    if neighbors in [2, 3]:
                        board[i][j] = 3
                elif neighbors == 3:
                    board[i][j] = 2
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1