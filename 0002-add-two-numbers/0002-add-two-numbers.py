# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        answer = None
        l3 = None

        while l1 is not None and l2 is not None:
            summation = l1.val + l2.val + carry
            if answer is None:
                answer = ListNode(summation % 10, None)
                l3 = answer
            else:
                l3.next = ListNode(summation % 10, None)
                l3 = l3.next
            carry = summation // 10
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            summation = l1.val + carry
            l3.next = ListNode(summation % 10, None)
            l3 = l3.next
            carry = summation // 10
            l1 = l1.next

        while l2 is not None:
            summation = l2.val + carry
            l3.next = ListNode(summation % 10, None)
            l3 = l3.next
            carry = summation // 10
            l2 = l2.next
        
        if carry:
            l3.next = ListNode(carry, None)

        return answer