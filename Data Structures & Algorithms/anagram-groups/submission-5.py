class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs: 
            counts = [0] * 26
            for char in s: 
                counts[ord(char) - ord('a')] += 1
            counts = tuple(counts)
            if counts in anagrams: 
                anagrams[counts].append(s)
            else: 
                anagrams[counts] = []
                anagrams[counts].append(s)
        return list(anagrams.values())