# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        stack1 = []
        stack2 = []

        stack1.append(root)

        while len(stack1):
            stack2.append(stack1.pop())

            if stack2[-1].left is not None:
                stack1.append(stack2[-1].left)            

            if stack2[-1].right is not None:
                stack1.append(stack2[-1].right)
        
        stack2.reverse()
        
        return [node.val for node in stack2]