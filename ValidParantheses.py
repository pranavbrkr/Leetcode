# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if len(stack):
                    popped_bracket = stack.pop()
                else:
                    return False
                print(popped_bracket)
                if (bracket == ')' and popped_bracket == '(') or (bracket == ']' and popped_bracket == '[') or (bracket == '}' and popped_bracket == '{'):
                    continue
                else:
                    return False

        if len(stack):
            return False
        else:
            return True