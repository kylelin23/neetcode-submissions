class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)): 
            encoded += strs[i]
            encoded += ';'
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ''
        for c in s: 
            if c != ';': 
                word += c
            else: 
                decoded.append(word)
                word = ''
        return decoded