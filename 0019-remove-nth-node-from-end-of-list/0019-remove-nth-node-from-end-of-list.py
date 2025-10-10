# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        count = 0

        # move the right n times
        while count < n:
            right = right.next
            count += 1
        

        # move right and left until right is None
        while right:
            right = right.next
            left = left.next
        

        # link left to its further neighbor
        left.next = left.next.next

        return dummy.next