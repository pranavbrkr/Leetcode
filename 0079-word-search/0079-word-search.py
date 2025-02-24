class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set()
        word_len = len(word)

        def dfs(row, col, index):
            if index >= word_len:
                return True
            
            if (row >= m or
               col >= n or 
               row < 0 or
               col < 0 or 
               board[row][col] != word[index] or 
               (row, col) in path):
                return False
            
            path.add((row, col))

            dfs_result = (dfs(row + 1, col, index + 1) or
                         dfs(row - 1, col, index + 1) or
                         dfs(row, col + 1, index + 1) or
                         dfs(row, col - 1, index + 1))
            
            path.remove((row, col))
            
            return dfs_result
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False