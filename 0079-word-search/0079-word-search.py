class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set() 

        def dfs(r, c, index):
            if index == len(word):
                return True
            
            if r < 0 or c < 0 or r >= m or c >= n or word[index] != board[r][c] or ((r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, index + 1) or
                  dfs(r - 1, c, index + 1) or
                  dfs(r, c + 1, index + 1) or
                  dfs(r, c - 1, index + 1))
            path.remove((r, c))
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False