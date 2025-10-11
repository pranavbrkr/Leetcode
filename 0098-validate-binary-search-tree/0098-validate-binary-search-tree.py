# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        q = deque()
        q.append((root, float('-inf'), float('inf')))

        while q:
            node, left_val, right_val = q.popleft()

            if not (left_val < node.val < right_val):
                return False
            
            if node.left:
                q.append((node.left, left_val, node.val))
            if node.right:
                q.append((node.right, node.val, right_val))
        
        return True