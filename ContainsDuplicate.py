# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        answer = False

        for number in nums:
            if str(number) in map:
                answer = True
                break
            else:
                map[str(number)] = True

        return answer