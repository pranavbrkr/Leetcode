"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        copy_head = None
        copy_curr = None
        node_map = dict()

        while curr is not None:
            if copy_curr is None:
                copy_curr = Node(curr.val)
                copy_head = copy_curr
            else:
                copy_curr.next = Node(curr.val)
                copy_curr = copy_curr.next
            
            node_map[curr] = copy_curr
            curr = curr.next
        
        curr = head
        copy_curr = copy_head

        while curr is not None:
            if curr.random is None:
                copy_curr.random = None
            else:
                copy_curr.random = node_map[curr.random]
            copy_curr = copy_curr.next
            curr = curr.next


        return copy_head