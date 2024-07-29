# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkBoundaries(self, root: Optional[TreeNode], lbound, rbound) -> bool:
        if root is None:
            return True
        
        if lbound < root.val < rbound:
            return self.checkBoundaries(root.left, lbound, root.val) and self.checkBoundaries(root.right, root.val, rbound)
        else:
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBoundaries(root, float('-inf'), float('inf'))