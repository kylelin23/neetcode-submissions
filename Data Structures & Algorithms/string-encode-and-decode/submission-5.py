class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: 
            result += str(len(s))
            result += ';'
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        length = ''
        result = []
        i = 0
        while i < len(s): 
            if s[i] == ';': 
                length = int(length)
                result.append(s[i + 1: i + 1 + length])
                i = i + 1 + length
                length = ''
            else: 
                length += s[i]
                i += 1
        return result
