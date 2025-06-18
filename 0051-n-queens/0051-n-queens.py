class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        col = set()
        pos_diag = set()
        neg_diag = set()

        board = [['.'] * n for _ in range(n)]

        def backtrack(c):
            if c == n:
                copy = ["".join(row) for row in board]
                answer.append(copy)
                return
            
            for r in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    return
                
                board[r][c] = 'Q'
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(c + 1)
                
                board[r][c] = '.'
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

            return

        backtrack(0)
        return answer