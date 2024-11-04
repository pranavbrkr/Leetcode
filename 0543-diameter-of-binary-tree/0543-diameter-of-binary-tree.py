# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    result = 0

    def DFS(self, node) -> int:
        if node is None:
            return 0
        
        left_height = self.DFS(node.left)
        right_height = self.DFS(node.right)

        self.result = (left_height + right_height) if (left_height + right_height) > self.result else self.result

        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        left_height = self.DFS(root.left)
        right_height = self.DFS(root.right)

        self.result = (left_height + right_height) if (left_height + right_height) > self.result else self.result

        return self.result