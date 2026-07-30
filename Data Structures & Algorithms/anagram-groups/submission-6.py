class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs: 
            count = [0] * 26
            for char in s: 
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            if count not in anagrams: 
                anagrams[count] = []
            anagrams[count].append(s)
        return list(anagrams.values())