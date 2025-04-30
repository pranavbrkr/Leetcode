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
        # Split list into two
        list1 = head
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None

        # Reverse list2
        prev, curr = None, list2

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        list2 = prev

        # Merge two lists
        curr = head
        curr2 = list2
        prev = None
        prev2 = None

        while curr2:
            prev = curr
            curr = curr.next
            prev2 = curr2
            curr2 = curr2.next
            prev2.next = curr
            prev.next = prev2