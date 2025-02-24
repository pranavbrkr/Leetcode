# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def checkSymmetry(left_tree, right_tree):
            if not left_tree and not right_tree:
                return True
            
            if not left_tree or not right_tree or left_tree.val != right_tree.val:
                return False
            
            return (checkSymmetry(left_tree.left, right_tree.right) and
                   checkSymmetry(left_tree.right, right_tree.left))
        

        return checkSymmetry(root.left, root.right)