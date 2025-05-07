class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if dp[i]:
                    break
                if ((i + len(word) <= n) and s[i:i + len(word)] == word):
                    dp[i] = dp[i + len(word)]
        
        return dp[0]