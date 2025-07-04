class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]

        dp[0][0] = True
        for j in range(1, len(s) + 1):
            dp[0][j] = False
        
        for i in range(1, len(p) + 1):
            dp[i][0] = True
            for x in range(1, i + 1):
                if p[x - 1] != "*":
                    dp[i][0] = False
                    break
        
        for i in range(1, len(p) + 1):            
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    dp[i][j]  = dp[i - 1][j] or dp[i][j - 1]
                elif p[i - 1] == "?" or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
        
        return dp[len(p)][len(s)]
            
        #     if p[i] == "*":
        #         dp[i][j] = recursion(i - 1, j) or recursion(i, j - 1)
        #     elif p[i] == "?" or p[i] == s[j]:
        #         dp[i][j] = recursion(i - 1, j - 1)
        #     else:
        #         dp[i][j] = False
            
        #     return dp[i][j]
        
        # return recursion(len(p) - 1, len(s) - 1)