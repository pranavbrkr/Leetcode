class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        n = len(nums)

        for i in range(n - 1, -1, -1):
            if (i + nums[i]) >= goal:
                goal = i
        
        return True if goal == 0 else False