  # https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        inorder = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                inorder.append(curr.val)
                curr = curr.right
            else:
                break
        
        return inorder