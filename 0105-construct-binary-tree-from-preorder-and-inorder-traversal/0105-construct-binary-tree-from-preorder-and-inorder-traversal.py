# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_index = inorder.index(preorder[0])
        node = TreeNode(preorder[0])

        node.left = self.buildTree(preorder[1: root_index + 1], inorder[:root_index])
        node.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])

        return node