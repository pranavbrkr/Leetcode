class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        m, n = len(board), len(board[0])
        path = set()


        def dfs(row, col, word_index):
            if word_index == word_len:
                return True
            
            if row < 0 or row >= m or col < 0 or col >= n or (row, col) in path or board[row][col] != word[word_index]:
                return False
            
            path.add((row, col))
            dfs_result = dfs(row + 1, col, word_index + 1) or dfs(row - 1, col, word_index + 1) or dfs(row, col + 1, word_index + 1) or dfs(row, col - 1, word_index + 1)
            path.remove((row, col))
            
            return dfs_result
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False