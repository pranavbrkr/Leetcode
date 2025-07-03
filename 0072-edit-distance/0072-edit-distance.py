class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        prev_dp = [0 for _ in range(len(word2) + 1)]

        for j in range(len(word2) + 1):
            prev_dp[j] = j
        
        for i in range(1, len(word1) + 1):
            curr_dp = [i]
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr_dp.append(prev_dp[j - 1])
                else:
                    curr_dp.append(1 + min(curr_dp[j - 1], prev_dp[j], prev_dp[j - 1]))
            
            prev_dp = curr_dp
        
        return prev_dp[len(word2)]

        
        # def recursion(i, j):
        #     if j < 0:
        #         return i + 1
        #     if i < 0:
        #         return j + 1

        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     if word1[i] == word2[j]:
        #         dp[i][j] = recursion(i - 1, j - 1)
        #         return dp[i][j]
        #     else:
        #         dp[i][j] =  1 + min(
        #             recursion(i, j - 1), # insert
        #             recursion(i - 1, j), # delete
        #             recursion(i - 1, j - 1), # replace
        #         )
        #         return dp[i][j]
        
        return recursion(len(word1) - 1, len(word2) - 1)