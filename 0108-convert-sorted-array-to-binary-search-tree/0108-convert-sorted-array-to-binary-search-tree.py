# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createNode(l, r):
            if l > r:
                return None
            
            m = (l + r) // 2
            node = TreeNode(nums[m])
            node.left = createNode(l, m - 1)
            node.right = createNode(m + 1, r)

            return node
        
        return createNode(0, len(nums) - 1)