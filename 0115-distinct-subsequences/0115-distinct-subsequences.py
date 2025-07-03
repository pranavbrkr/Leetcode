class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[len(s)][len(t)]


        # def recursion(i, j):
            
        #     if j < 0:
        #         return 1

        #     if i < 0:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s[i] == t[j]:
        #         dp[i][j] = recursion(i - 1, j - 1) + recursion(i - 1, j)
        #     else:
        #         dp[i][j] = recursion(i - 1, j)
            
        #     return dp[i][j]
        
        # return recursion(len(s) - 1, len(t) - 1)