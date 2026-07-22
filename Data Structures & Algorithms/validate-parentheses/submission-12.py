class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end_to_start = {')': '(', '}': '{', ']': '['}
        for char in s: 
            if char in end_to_start: 
                if len(stack) == 0 or stack[-1] != end_to_start[char]: 
                    return False
                else: 
                    stack.pop()
            else: 
                stack.append(char)
        return len(stack) == 0