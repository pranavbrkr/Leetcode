# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None
        
        ret = TreeNode(root.val)
        ret.left = self.invertTree(root.right)
        ret.right = self.invertTree(root.left)

        return ret