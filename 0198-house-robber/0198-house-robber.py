class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = [-1] * len(nums)
        cache[0] = nums[0]

        for i in range(1, len(nums)):
            pick = nums[i]
            if i > 1:
                pick += cache[i - 2]
            non_pick = cache[i - 1]

            cache[i] = max(pick, non_pick)

        return cache[-1]