class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs: 
            counts = [0] * 26
            for c in s: 
                counts[ord(c) - ord('a')] += 1
            counts = tuple(counts)
            
            if counts in anagrams: 
                anagrams[counts].append(s)
            else: 
                words = []
                words.append(s)
                anagrams[counts] = words
            
        return list(anagrams.values())