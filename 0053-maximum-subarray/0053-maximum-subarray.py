class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        curr_sum = 0

        for number in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += number
            max_sum = max(max_sum, curr_sum)
    
        return max_sum