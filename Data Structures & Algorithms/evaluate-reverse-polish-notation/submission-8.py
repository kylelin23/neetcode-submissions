class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {'+', '-', '*', '/'}
        for token in tokens: 
            if token in symbols: 
                print(stack)
                if token == '+': 
                    result = int(stack[-1]) + int(stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif token == '-': 
                    result = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif token == '*': 
                    result = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                else: 
                    result = int(int(stack[-2]) / int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(result)
            else: 
                stack.append(int(token))
        return stack[-1]