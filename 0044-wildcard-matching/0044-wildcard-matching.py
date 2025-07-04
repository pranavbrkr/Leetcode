class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        
        dp = [[-1 for _ in range(len(s))] for _ in range(len(p))]
        def recursion(i, j):
            if i < 0 and j < 0:
                return True
            
            if i < 0 and j >= 0:
                return False
            
            if j < 0 and i >= 0:
                while i >= 0:
                    if p[i] != "*":
                        return False
                    i -= 1                
                return True

            if dp[i][j] != -1:
                return dp[i][j]
            
            if p[i] == "*":
                dp[i][j] = recursion(i - 1, j) or recursion(i, j - 1)
            elif p[i] == "?" or p[i] == s[j]:
                dp[i][j] = recursion(i - 1, j - 1)
            else:
                dp[i][j] = False
            
            return dp[i][j]
        
        return recursion(len(p) - 1, len(s) - 1)