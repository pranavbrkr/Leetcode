class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        prev_dp = [0 for _ in range(len(t) + 1)]
        prev_dp[0] = 1
    

        for i in range(1, len(s) + 1):
            curr_dp = [1]
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    curr_dp.append(prev_dp[j - 1] + prev_dp[j])
                else:
                    curr_dp.append(prev_dp[j])
            
            prev_dp = curr_dp.copy()
        
        return prev_dp[len(t)]