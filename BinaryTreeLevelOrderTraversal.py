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
            nextLevel = []

            while len(currNodes):
                ele = currNodes.pop(0)
                currLevel.append(ele.val)
                if ele.left:
                    nextLevel.append(ele.left)
                if ele.right:
                    nextLevel.append(ele.right)
            answer.append(currLevel)
            currNodes = nextLevel

        return answer