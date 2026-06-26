class Solution:
    def isValid(self, s: str) -> bool:
        endToClose = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s: 
            if c in endToClose: 
                if len(stack) == 0 or endToClose[c] != stack[-1]: 
                    return False
                stack.pop()
            else: 
                stack.append(c)
        return len(stack) == 0