# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:                
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                answer.append(level)
        
        return answer