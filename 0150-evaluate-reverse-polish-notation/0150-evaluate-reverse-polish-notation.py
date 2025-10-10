class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                val2 = stack.pop()
                val1 = stack.pop()
                if t == '+':
                    stack.append(val1 + val2)
                elif t == '-':
                    stack.append(val1 - val2)
                elif t == '*':
                    stack.append(val1 * val2)
                else:
                    stack.append(int(val1 / val2))
            else:
                stack.append(int(t))
        
        return stack[-1]