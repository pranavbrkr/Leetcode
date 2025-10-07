class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        breakpoint = -1

        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                breakpoint = i - 1
                break
        
        if breakpoint == -1:
            nums.reverse()
            return
        
        for i in range(n - 1, breakpoint - 1, -1):
            if nums[i] > nums[breakpoint]:
                nums[i], nums[breakpoint] = nums[breakpoint], nums[i]
                break

        nums[breakpoint + 1:] = reversed(nums[breakpoint + 1:])
        return