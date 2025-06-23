class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        temp = [0] * n
        temp[0] = 1
        for i in range(m):
            dp = [-1] * n
            for j in range(n):
                if j == 0:
                    dp[j] = temp[j]
                else:
                    dp[j] = dp[j - 1] + temp[j]
            temp = dp
        
        return temp[-1]