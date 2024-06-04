# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        product = 1
        zero_freq = 0

        for num in nums:
            if num == 0:
                zero_freq += 1
                continue
            else:
                product *= num

        answer = []

        for num in nums:
            if num == 0:
                if zero_freq > 1:
                    answer.append(0)
                else:
                    answer.append(product)
            else:
                if zero_freq:
                    answer.append(0)
                else:
                    answer.append(product // num)

        return answer