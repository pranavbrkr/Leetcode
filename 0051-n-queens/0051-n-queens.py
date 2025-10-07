class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        col_set = set()
        pos_diag = set()
        neg_diag = set()
        
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                answer.append(copy)
                return
            
            for col in range(n):
                if col in col_set or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                board[row][col] = 'Q'
                col_set.add(col)
                pos_diag.add((row + col))
                neg_diag.add((row - col))

                backtrack(row + 1)

                board[row][col] = '.'
                col_set.remove(col)
                pos_diag.remove((row + col))
                neg_diag.remove((row - col))

            return
        
        backtrack(0)
        return answer