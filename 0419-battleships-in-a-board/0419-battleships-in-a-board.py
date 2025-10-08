class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        battleships = 0
        rows, cols = len(board), len(board[0])

        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == '.' or (r, c) in visited:
                return
            
            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and board[i][j] == 'X':
                    dfs(i, j)
                    battleships += 1
        
        return battleships