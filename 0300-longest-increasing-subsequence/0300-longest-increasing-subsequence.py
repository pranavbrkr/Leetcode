class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for index in range(n - 1, -1, -1):
            for prev_index in range(index - 1, -2, -1):
                not_take = 0 + dp[index + 1][prev_index + 1]
                take = float('-inf')
                if prev_index == -1 or nums[index] > nums[prev_index]:
                    take = 1 + dp[index + 1][index + 1]
                dp[index][prev_index + 1] = max(not_take, take)
        
        return dp[0][0]