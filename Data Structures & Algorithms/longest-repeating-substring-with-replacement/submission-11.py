class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 1
        counts = {}
        counts[s[0]] = 1
        result = 1
        maxCount = 1
        while end < len(s): 
            # Updating Dictionary
            if s[end] in counts: 
                counts[s[end]] += 1
            else: 
                counts[s[end]] = 1

            # Updating max count
            maxCount = max(maxCount, counts[s[end]])

            # If too many replacements
            if (end - start + 1) - maxCount > k: 
                counts[s[start]] -= 1
                start += 1
                end += 1

            # If you can replace, update result
            else: 
                result = max(result, end - start + 1)
                end += 1
            print("Result: " + str(result))
                
        return result