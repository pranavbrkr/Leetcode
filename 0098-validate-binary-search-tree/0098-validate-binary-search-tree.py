# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, left_val, right_val):
            if not node:
                return True
            
            if not (left_val < node.val < right_val):
                return False
            
            return isValid(node.left, left_val, node.val) and isValid(node.right, node.val, right_val)
        
        return isValid(root, float('-inf'), float('inf'))