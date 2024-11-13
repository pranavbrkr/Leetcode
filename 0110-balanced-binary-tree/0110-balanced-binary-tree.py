# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedUtil(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_height = self.isBalancedUtil(root.left)
        right_height = self.isBalancedUtil(root.right)

        if left_height == -1 or right_height == -1:
            return -1
        elif abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height + 1, right_height + 1)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.isBalancedUtil(root) == -1:
            return False
        else:
            return True