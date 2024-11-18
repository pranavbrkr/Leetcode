# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0

    def goodNodesUtil(self, root: TreeNode, greatestValue: int) -> None:
        if root is None:
            return
        if greatestValue <= root.val:
            self.answer += 1
            print(f"answer is {self.answer} at {root.val}")
            self.goodNodesUtil(root.left, root.val)
            self.goodNodesUtil(root.right, root.val)
        else:
            self.goodNodesUtil(root.left, greatestValue)
            self.goodNodesUtil(root.right, greatestValue)

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.goodNodesUtil(root, float('-inf'))
        return self.answer