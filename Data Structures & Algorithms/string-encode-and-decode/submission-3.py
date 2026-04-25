class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + ";"
            encoded += s
        print(encoded)
        return encoded
        

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s): 
            j = i
            length = ''
            while s[j] != ';': 
                length += s[j]
                j += 1
            decoded.append(s[j + 1: j + 1 + int(length)])
            i = j + 1 + int(length)
        return decoded