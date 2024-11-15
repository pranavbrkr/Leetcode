# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        level_traversal = []
        answer = []

        if root is None:
            return answer
        
        level_traversal.append(root)
        level_traversal.append('*')

        while len(level_traversal) is not 0:
            if level_traversal[0] is '*':
                level_traversal.pop(0)
                answer.append(popped_ele.val)
                if len(level_traversal) is not 0:
                    level_traversal.append('*')
            else:
                popped_ele = level_traversal.pop(0)
                if popped_ele.left is not None:
                    level_traversal.append(popped_ele.left)
                if popped_ele.right is not None:
                    level_traversal.append(popped_ele.right)
            print(level_traversal)
            print(answer)

        return answer