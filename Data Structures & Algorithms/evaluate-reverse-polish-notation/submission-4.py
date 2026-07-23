class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}
        for t in tokens: 
            if t in operands: 
                if t == '+': 
                    total = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(total)
                elif t == '-': 
                    total = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(total)
                elif t == '*': 
                    total = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(total)
                else: 
                    total = int(stack[-2]) / int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(total)
            else: 
                stack.append(t)
        return int(stack[-1])