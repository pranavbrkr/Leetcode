# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodesUtil(node, max_value):
            if not node:
                return 0
            
            answer = 1 if node.val >= max_value else 0
            
            max_value = max(max_value, node.val)
            
            answer += goodNodesUtil(node.left, max_value)
            answer += goodNodesUtil(node.right, max_value)
            
            return answer
        
        return goodNodesUtil(root, root.val)