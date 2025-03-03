class TicTacToe:

    def __init__(self, n: int):
        self.rows = defaultdict(int)
        self.columns = defaultdict(int)
        self.left_diag = 0
        self.right_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        number = -1 if player == 1 else 1
        self.rows[row] += number
        self.columns[col] += number
        if row == col:
            self.left_diag += number
        if row + col == self.n - 1:
            self.right_diag += number
        
        if max(abs(self.rows[row]), abs(self.columns[col]), abs(self.left_diag), abs(self.right_diag)) == self.n:
            return player

        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)