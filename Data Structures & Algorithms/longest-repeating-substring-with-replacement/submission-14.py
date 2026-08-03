class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        maxFreq = 0
        counts = {}
        result = 0;
        for end in range(len(s)): 
            if s[end] in counts: 
                counts[s[end]] += 1
            else: 
                counts[s[end]] = 1
            
            maxFreq = max(maxFreq, counts[s[end]])
            while end - start + 1 - maxFreq > k: 
                counts[s[start]] -= 1
                start += 1

            result = max(result, end - start + 1)
        return result