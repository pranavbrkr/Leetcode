class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = [-1] * len(nums)
        cache[0] = nums[0]

        def recursion(index):
            if cache[index] != -1:
                return cache[index]
            if index == 0:
                return cache[index]
            
            if index < 0:
                return 0
            
            pick = nums[index] + recursion(index - 2)
            non_pick = recursion(index - 1)

            cache[index] = max(pick, non_pick)
            return cache[index]

        return recursion(len(nums) - 1)