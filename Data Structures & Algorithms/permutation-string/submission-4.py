class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        start = 0
        end = len(s1) - 1
        s1Counts = [0] * 26
        s2Counts = [0] * 26

        for c in s1: 
            s1Counts[ord(c) - ord('a')] += 1
        
        temp = start
        while temp <= end: 
            s2Counts[ord(s2[temp]) - ord('a')] += 1
            temp += 1

        while end < len(s2): 
            print(s2Counts)
            if s1Counts == s2Counts: 
                return True

            s2Counts[ord(s2[start]) - ord('a')] -= 1
            start += 1
            end += 1
            if end == len(s2): 
                return False
            s2Counts[ord(s2[end]) - ord('a')] += 1
        
        return False
