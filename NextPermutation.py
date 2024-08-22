# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        breakpoint = -1
        for i in range(n - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                breakpoint = i - 1
                break

        if breakpoint == -1:
            nums = nums.sort()
            return

        comp = nums[breakpoint:].index(max(nums[breakpoint:])) + len(nums[:breakpoint])

        for i in range(n - 1, breakpoint - 1, -1):
            if nums[i] < nums[comp] and nums[i] > nums[breakpoint]:
                comp = i

        nums[breakpoint], nums[comp] = nums[comp], nums[breakpoint]

        nums[breakpoint + 1:] = sorted(nums[breakpoint + 1:])