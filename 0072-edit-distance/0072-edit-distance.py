class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        def recursion(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = recursion(i - 1, j - 1)
            else:
                dp[i][j] = 1 + min(
                    recursion(i, j - 1),
                    recursion(i - 1, j),
                    recursion(i - 1, j - 1)
                )
            return dp[i][j]
        
        return recursion(len(word1) - 1, len(word2) - 1)