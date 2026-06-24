class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = start
        maxCount = 0
        counts = {}
        result = 0
        while end < len(s): 
            # Update counts
            if s[end] in counts: 
                counts[s[end]] += 1
            else: 
                counts[s[end]] = 1
            
            # Update max count
            if counts[s[end]] > maxCount: 
                maxCount = counts[s[end]]
            
            if k >= end - start + 1 - maxCount: 
                length = end-start + 1
                if length > result: 
                    result = length
                
                
            else: 
                counts[s[start]] -= 1
                start += 1
            end += 1

        return result