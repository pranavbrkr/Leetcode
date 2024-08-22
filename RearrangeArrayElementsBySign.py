# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = [x for x in nums if  x < 0]
        pos = [x for x in nums if x > 0]
        
        res = []

        n = len(nums) // 2

        for i in range(n):
            res.append(pos[i])
            res.append(neg[i])

        return res