# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node_list = deque([])

        if head.next == None:
            return head

        # Add all the nodes to a deque
        curr = head
        while head != None:
            head = curr.next
            curr.next = None
            node_list.append(curr)
            curr = head
        print(node_list)

        # Pop the front and back elements alternatively and create a list
        pop_front = True
        while len(node_list):
            if pop_front:
                if not head:
                    head = node_list.popleft()
                    curr = head
                else:
                    curr.next = node_list.popleft()
                    curr = curr.next
            else:
                curr.next = node_list.pop()
                curr = curr.next
            
            pop_front = not pop_front

        return head