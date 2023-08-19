# https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        returnValue = 0;

        for i in range(len(nums)):
            returnValue = returnValue ^ nums[i]

        return returnValue