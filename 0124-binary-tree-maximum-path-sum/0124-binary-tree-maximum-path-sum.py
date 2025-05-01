# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = root.val

        def dfs(node):
            if not node:
                return 0

            left_height = max(dfs(node.left), 0)
            right_height = max(dfs(node.right), 0)

            self.answer = max(self.answer, node.val + left_height + right_height)

            return (node.val + max(left_height, right_height))

        dfs(root)
        return self.answer