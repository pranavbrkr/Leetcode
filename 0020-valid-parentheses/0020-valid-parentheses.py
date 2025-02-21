class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                popped_bracket = stack.pop()
                if popped_bracket is "(" and bracket is not ")":
                    return False
                elif popped_bracket is "[" and bracket is not "]":
                    return False
                elif popped_bracket is "{" and bracket is not "}":
                    return False
        
        if stack:
            return False
        
        return True