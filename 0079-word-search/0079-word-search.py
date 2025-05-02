class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        m, n = len(board), len(board[0])
        path = set()

        def dfs(index, row, col):
            if index >= word_len:
                return True
            
            if row >= m or col >= n or row < 0 or col < 0 or board[row][col] != word[index] or (row, col) in path:
                return False
            
            path.add((row, col))
            dfs_result = (dfs(index + 1, row + 1, col) or
                         dfs(index + 1, row - 1, col) or
                         dfs(index + 1, row, col + 1) or
                         dfs(index + 1, row, col - 1))
            
            path.remove((row, col))
            return dfs_result
        
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        
        return False