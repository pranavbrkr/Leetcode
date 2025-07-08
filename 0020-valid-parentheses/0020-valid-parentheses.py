class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for bracket in s:
            if bracket in bracket_map:
                if stack and stack[-1] == bracket_map[bracket]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(bracket)
        
        return True if not stack else False