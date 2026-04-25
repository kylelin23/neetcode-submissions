class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs: 
            counts = [0] * 26
            for c in s: 
                counts[ord(c) - ord('a')] += 1
            if tuple(counts) in d: 
                d[tuple(counts)].append(s)
            else: 
                d[tuple(counts)] = [s]
        return(list(d.values()))