# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(root, left_bound, right_bound):
            if root is None:
                return True
            
            if root.val < right_bound and root.val > left_bound:
                return checkBST(root.left, left_bound, root.val) and checkBST(root.right, root.val, right_bound)

            return False
        
        return checkBST(root, float('-inf'), float('inf'))