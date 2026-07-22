class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = 0
        end = 1
        while end <= len(s): 
            cur = s[start:end]
            if len(cur) != len(set(cur)): 
                start += 1
            else: 
                result = max(result, len(cur))
                end += 1
        return result