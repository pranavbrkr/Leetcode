class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for index in range(n):
            for prev in range(index):
                if nums[index] > nums[prev] and (1 + dp[prev]) > dp[index]:
                    dp[index] = 1 + dp[prev]
                    count[index] = count[prev]
                elif nums[index] > nums[prev] and (1 + dp[prev]) == dp[index]:
                    count[index] += count[prev]

        
        max_len = max(dp)

        num = 0
        for i in range(n):
            if dp[i] == max_len:
                num += count[i]
        
        return num