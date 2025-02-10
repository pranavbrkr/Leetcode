class Solution:
    def rob(self, nums: List[int]) -> int:

        def robber1(nums):
            rob1, rob2 = 0, 0
            
            for num in nums:
                newRob = max(rob2, num + rob1)
                rob1= rob2
                rob2 = newRob
            
            return rob2
        
        return max(nums[0], robber1(nums[1:]), robber1(nums[:-1]))
