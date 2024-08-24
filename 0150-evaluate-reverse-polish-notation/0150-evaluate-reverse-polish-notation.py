import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    div = op1 / op2
                    if div < 0:
                        stack.append(math.ceil(div))
                    else:
                        stack.append(op1 // op2)
            
        return stack[0]