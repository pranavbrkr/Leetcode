class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN, closeN):
            # 
            if openN == closeN == n:
                res.append(''.join(stack))
                print(''.join(stack))
            if openN < n:
                #increment the opening bracket
                stack.append('(')
                print(stack)
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                #increment the closing bracket
                stack.append(')')
                print(stack)
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0, 0)
        return res