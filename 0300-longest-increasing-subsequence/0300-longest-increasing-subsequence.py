class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxi = 1
        backtrack = [i for i in range(n)]

        for index in range(n):
            for prev in range(index):
                if nums[prev] < nums[index] and (1 + dp[prev]) > dp[index]:
                    dp[index] = 1 + dp[prev]
                    backtrack[index] = prev
            maxi = max(maxi, dp[index])

        
        return maxi