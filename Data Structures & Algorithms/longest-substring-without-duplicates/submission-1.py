class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxLength = 0

        while end < len(s): 
            while len(s[start:(end + 1)]) != len(set(s[start:(end + 1)])): 
                # if there is a duplicate
                start += 1
            if end - start + 1 > maxLength: 
                maxLength = end - start + 1
            end += 1
        return maxLength