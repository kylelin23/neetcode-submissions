class Solution:

    def isAlphaNumeric(self, c): 
        return (ord(c) >= ord('a') and ord(c) < ord('z')) or (ord(c) >= ord('A') and ord(c) < ord('Z')) or (ord(c) >= ord('0') and ord(c) < ord('9'))

    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2: 
            while not self.isAlphaNumeric(s[p1]) and p1 < p2: 
                p1 += 1
            while not self.isAlphaNumeric(s[p2]) and p1 < p2: 
                p2 -= 1
            if not s[p1].lower() == s[p2].lower(): 
                return False

            p1 += 1
            p2 -= 1
        return True