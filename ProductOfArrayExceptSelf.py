# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix = 1

        answer = []
        n = len(nums)

        for i in range(n):
            answer.append(prefix)
            prefix = prefix * nums[i]

        postfix = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i]  * postfix
            postfix = postfix * nums[i]

        return answer