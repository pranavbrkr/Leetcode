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
        node_dict = {}

        while curr:
            if not copy_head:
                copy_head = Node(curr.val)
                copy_curr = copy_head
            else:
                copy_curr.next = Node(curr.val)
                copy_curr = copy_curr.next
            
            node_dict[curr] = copy_curr
            curr = curr.next
        

        copy_curr = copy_head
        curr = head

        while curr:
            if not curr.random:
                copy_curr.random = None
            else:
                copy_curr.random = node_dict[curr.random]
            
            curr = curr.next
            copy_curr = copy_curr.next
        
        return copy_head