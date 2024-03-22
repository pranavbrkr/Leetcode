# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dic = defaultdict(lambda: 0)

        len_s = len(s)
        len_t = len(t)

        for i in range(len_s):
            dic[s[i]] += 1
        
        for i in range(len_t):
            dic[t[i]] -= 1

        for key, value in dic.items():
            if value:
                return False
        
        return True