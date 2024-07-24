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

        # Use fast and slow pointer to find the middle of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None

        # Reverse the second list
        curr = list2
        prev = None

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        list2 = prev

        # Now merge the nodes alternatively
        prev2 = None
        curr2 = list2

        prev = None
        curr = head
        while curr2:
            prev = curr
            curr = curr.next
            prev2 = curr2
            curr2 = curr2.next
            prev2.next = curr
            prev.next = prev2