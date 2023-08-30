# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) is 0:
            return None
        else:
            index = len(nums) / 2
            return TreeNode(nums[index], self.sortedArrayToBST(nums[:index]), self.sortedArrayToBST(nums[index+1:]))