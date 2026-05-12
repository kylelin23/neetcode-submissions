class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        maxLength = 0
        maxCount = 0
        counts = {}
        while end < len(s): 
            if s[end] in counts: 
                counts[s[end]] += 1
            else: 
                counts[s[end]] = 1
            
            if counts[s[end]] > maxCount: 
                maxCount = counts[s[end]]
            
            if end + 1 - start - maxCount <= k: 
                if end - start + 1 > maxLength: 
                    maxLength = end - start + 1
            else: 
                counts[s[start]] -= 1
                start += 1
            

            end += 1
        return maxLength