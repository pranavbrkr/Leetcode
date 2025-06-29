class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def recursion(i, j):
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i] == text2[j]:
                dp[i][j] = 1 + recursion(i - 1, j - 1)
                return dp[i][j]
            
            dp[i][j] = max(recursion(i - 1, j), recursion(i, j - 1))
            return dp[i][j]
        
        return recursion(len(text1) - 1, len(text2) - 1)