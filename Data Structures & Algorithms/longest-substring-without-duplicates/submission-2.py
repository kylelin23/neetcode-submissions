class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        result = 0
        while end <= len(s) and start < end: 
            substring = s[start:end]
            print(substring)
            if len(list(substring)) != len(set(substring)): 
                # there are duplicates
                start += 1
            else: 
                if len(substring) > result: 
                    result = len(substring)
                end += 1
        return result
            