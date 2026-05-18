class Solution:
    def isValid(self, s: str) -> bool:
        endToClose = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s: 
            if c in endToClose: 
                if stack and stack[-1] == endToClose[c]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)
        if stack: 
            return False
        else: 
            return True