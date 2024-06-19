# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        answer = []
        for i in range(n):
            if i == 0:
                answer.append(1)
            elif i == 1:
                answer.append(2)
            else:
                answer.append(answer[i - 1] + answer[i - 2])

        return answer[-1]