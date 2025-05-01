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

        def checkSymmetry(lefttree, righttree):
            if not lefttree and not righttree:
                return True
            
            if lefttree and righttree and lefttree.val == righttree.val:
                return checkSymmetry(lefttree.left, righttree.right) and checkSymmetry(lefttree.right, righttree.left)
            else:
                return False
        
        return checkSymmetry(root.left, root.right)