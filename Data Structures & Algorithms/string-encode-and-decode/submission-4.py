class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: 
            result += str(len(s))
            result += ';'
            result += s
        print(result)
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != ';': 
                j += 1
            num = int(s[i:j])
            word = ""
            for k in range(j + 1, j + 1 + num): 
                word += s[k]
            result.append(word)
            i = j + 1 + num
        return result