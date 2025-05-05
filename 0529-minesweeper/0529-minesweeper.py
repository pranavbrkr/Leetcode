class Solution:
    def getAdjacentMines(self, board, x, y):
        num_mines = 0
        m = len(board)
        n = len(board[0])

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i >= 0 and i < m) and (j >= 0 and j < n) and board[i][j] == 'M':
                    num_mines += 1
        return num_mines

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board

        m = len(board)
        n = len(board[0])

        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            mines = self.getAdjacentMines(board, x, y)
            if mines:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if (i >= 0 and i < m) and (j >= 0 and j < n) and board[i][j] != 'B':
                            self.updateBoard(board, [i, j])
        return board