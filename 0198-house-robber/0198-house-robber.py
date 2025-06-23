class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            temp = max(prev, prev2 + nums[i])
            prev2 = prev
            prev = temp
        
        return prev