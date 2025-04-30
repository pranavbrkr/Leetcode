class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:
            if bracket in bracketmap:
                if stack and stack[-1] == bracketmap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return True if not stack else False