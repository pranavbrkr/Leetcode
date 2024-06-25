# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, h =  0, n - 1

        while l < h:
            mid = (l + h) // 2
            
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid

        return nums[l]