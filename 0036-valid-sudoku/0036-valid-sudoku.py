class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        n = len(board)

        for i in range(n):
            rows = set()
            cols = set()
            a = i // 3
            for j in range(n):
                b = j // 3

                if board[i][j] in rows:
                    return False
                elif board[i][j] != '.':
                    rows.add(board[i][j])
                
                if board[j][i] in cols:
                    return False
                elif board[j][i] != '.':
                    cols.add(board[j][i])
                
                if board[i][j] in squares[(a, b)]:
                    return False
                elif board[i][j] != '.':
                    squares[(a, b)].add(board[i][j])
        
        return True