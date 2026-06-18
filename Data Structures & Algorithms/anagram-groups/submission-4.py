class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs: 
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] += 1
            
            count = tuple(count)
            
            if count in result: 
                result[count].append(s)
            else: 
                result[count] = []
                result[count].append(s)
        return list(result.values())