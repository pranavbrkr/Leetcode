class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):
            rob1 = 0
            rob2 = 0

            for i in range(len(arr)):
                temp = max(rob1 + arr[i], rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))