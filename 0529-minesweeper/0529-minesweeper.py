class Solution:
    def getAdjacentMines(self, board, x, y):
        num_mines = 0
        for r in range(x - 1, x + 2):
            for c in range(y - 1, y + 2):
                if (r >= 0 and r < len(board) and
                    c >= 0 and c < len(board[0]) and
                    board[r][c] == 'M'):
                    num_mines += 1

        return num_mines

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            num_mines = self.getAdjacentMines(board, x, y)
            if num_mines:
                board[x][y] = str(num_mines)
            else:
                board[x][y] = 'B'
                for r in range(x - 1, x + 2):
                    for c in range(y - 1, y + 2):
                        if (r >= 0 and r < len(board) and
                            c >= 0 and c < len(board[0]) and
                            board[r][c] != 'B'):
                            self.updateBoard(board, [r, c])

        return board