class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            temp = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = temp
        
        return prev1