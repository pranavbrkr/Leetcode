class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Original | New | state
        #     0    |  0  |   0
        #     1    |  0  |   1
        #     0    |  1  |   2
        #     1    |  1  |   3

        rows, cols = len(board), len(board[0])

        def countNeighbours(r, c):
            num_neighbours = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or
                        i < 0  or j < 0 or i == rows or j == cols):
                        continue
                    if board[i][j] in [1, 3]:
                        num_neighbours += 1

            return num_neighbours

        for i in range(rows):
            for j in range(cols):
                num_neighbours = countNeighbours(i, j)

                if board[i][j]:
                    if num_neighbours in [2, 3]:
                        board[i][j] = 3
                elif num_neighbours == 3:
                    board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1