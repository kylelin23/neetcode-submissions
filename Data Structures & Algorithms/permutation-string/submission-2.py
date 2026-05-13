class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = start + len(s1) - 1
        matches = 0
        s1Counts = [0] * 26
        s2Counts = [0] * 26

        for letter in s1: 
            s1Counts[ord(letter) - ord('a')] += 1

        for letter in s2[start:end + 1]: 
            s2Counts[ord(letter) - ord('a')] += 1

        for i in range(26): 
            if s1Counts[i] == s2Counts[i]: 
                matches += 1
        
        
        while end < len(s2) - 1: 
            if matches == 26: 
                return True
            
            idx = ord(s2[start]) - ord('a')
            if s2Counts[idx] == s1Counts[idx]:
                matches -= 1
            s2Counts[idx] -= 1
            if s2Counts[idx] == s1Counts[idx]:
                matches += 1

            start += 1
            end += 1

            idx = ord(s2[end]) - ord('a')
            if s2Counts[idx] == s1Counts[idx]:
                matches -= 1
            s2Counts[idx] += 1
            if s2Counts[idx] == s1Counts[idx]:
                matches += 1





        return matches == 26
