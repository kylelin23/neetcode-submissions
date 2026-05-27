class Solution:
    def isValid(self, s: str) -> bool:
        endToClose = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s: 
            if char in endToClose: 
                if len(stack) > 0 and stack[-1] == endToClose[char]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)
        if len(stack) == 0: 
            return True
        else: 
            return False