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

        if not root:
            return root

        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)

            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    if i == queue_len - 1:
                        node.next = None
                    else:
                        node.next = queue[0]
                    queue.append(node.left)
                    queue.append(node.right)
        
        return root