"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        depth_map = {}

        def dfs(node, depth):
            if not node:
                return
            
            if depth not in depth_map:
                depth_map[depth] = node
            else:
                depth_map[depth].next = node
                depth_map[depth] = node

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return root