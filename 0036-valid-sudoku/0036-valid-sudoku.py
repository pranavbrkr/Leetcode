class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = {}

        for i in range(9):
            cols = set()
            rows = set()
            a = i // 3
            for j  in range(9):
                b = j // 3
                # check row
                if board[i][j] in rows:
                    return False
                elif board[i][j] != '.':
                    rows.add(board[i][j])
                
                # check column
                if board[j][i] in cols:
                    return False
                elif board[j][i] != '.':
                    cols.add(board[j][i])
                
                # check squares
                if (a, b) not in squares.keys():
                    squares[(a, b)] = set()
                
                if board[i][j] in squares[(a, b)]:
                    return False
                elif board[i][j] != '.':
                    squares[(a, b)].add(board[i][j])
        
        return True