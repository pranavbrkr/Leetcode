# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head.next == None:
            return head

        curr = head
        it = curr.next
        prev = curr

        while it != None and curr != None:

            while it.next != None:
                prev = it
                it = it.next
            
            prev.next = None
            it.next = curr.next
            curr.next = it

            curr = it.next
            if curr == None:
                break
            it = curr.next
            prev = curr

        return head