class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        

        answer = ""
        i, j = n1, n2
        while(i > 0 and j > 0):
            if str1[i - 1] == str2[j - 1]:
                answer += str1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                answer += str1[i - 1]
                i -= 1
            else:
                answer += str2[j - 1]
                j -= 1
        
        while i > 0:
            answer += str1[i - 1]
            i -= 1
        
        while j > 0:
            answer += str2[j - 1]
            j -= 1
        

        return answer[::-1]