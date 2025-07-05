class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxi = 1
        last_index = 0
        backtrack = [i for i in range(n)]

        for index in range(n):
            for prev in range(index):
                if nums[prev] < nums[index] and (1 + dp[prev]) > dp[index]:
                    dp[index] = 1 + dp[prev]
                    backtrack[index] = prev
            if dp[index] > maxi:
                maxi = dp[index]
                last_index = index


        lis = [nums[last_index]]

        while backtrack[last_index] != last_index:
            last_index = backtrack[last_index]
            lis.insert(0, nums[last_index])
        
        print(lis)
        return maxi