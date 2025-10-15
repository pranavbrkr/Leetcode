class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def backtrack(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = backtrack(i - 1, j - 1) + backtrack(i - 1, j)
            else:
                dp[(i, j)] = backtrack(i - 1, j)
            
            return dp[(i, j)]
        
        return backtrack(len(s) - 1, len(t) - 1)