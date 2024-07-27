# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        if root is None:
            return answer
        
        currNodes = [root]

        while len(currNodes):
            currLevel = []
            n = len(currNodes)

            while n:
                ele = currNodes.pop(0)
                currLevel.append(ele.val)
                if ele.left:
                    currNodes.append(ele.left)
                if ele.right:
                    currNodes.append(ele.right)
                n -= 1
            answer.append(currLevel)

        return answer