class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1) - 1
        s1counts = [0] * 26
        for c in s1: 
            s1counts[ord(c) - ord('a')] += 1
        
        s2counts = [0] * 26
        for c in s2[0:len(s1)]: 
            s2counts[ord(c) - ord('a')] += 1

        while end < len(s2): 
            if s1counts == s2counts: 
                return True
            s2counts[ord(s2[start]) - ord('a')] -= 1
            start += 1
            end += 1
            if end < len(s2): 
                s2counts[ord(s2[end]) - ord('a')] += 1

        return False