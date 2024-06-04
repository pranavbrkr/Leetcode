# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ""
        for letter in s:
            if letter.isalnum():
                if letter.isalpha():
                    new_string += letter.lower()
                else:
                    new_string += letter
            else:
                continue

        n = len(new_string)

        for i in range(n // 2):
            if new_string[i] != new_string[-1-i]:
                return False

        return True