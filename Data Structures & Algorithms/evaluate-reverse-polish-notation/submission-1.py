class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ['+', '*', '-', '/']
        for token in tokens: 
            print(stack)
            if token in symbols: 
                if token == '+': 
                    result = int(stack[-2]) + int(stack[-1])
                if token == '-': 
                    result = int(stack[-2]) - int(stack[-1])
                if token == '*': 
                    result = int(stack[-1]) * int(stack[-2])
                if token == '/': 
                    result = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            else: 
                stack.append(token)
        return int(stack[-1])