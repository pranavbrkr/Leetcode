# https://leetcode.com/problems/reverse-linked-list/

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            currNode = head
            prevNode = None

            while currNode is not None:
                tempNode = currNode
                currNode = currNode.next
                tempNode.next = prevNode
                prevNode = tempNode

            return prevNode
    