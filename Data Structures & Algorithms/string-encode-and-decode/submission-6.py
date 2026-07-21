class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: 
            result += str(len(s))
            result += ';'
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        p = 0
        result = []
        while p < len(s):
            num = ""
            while s[p] != ';': 
                num += s[p]
                p += 1
            p += 1
            string = ""
            for i in range(int(num)): 
                string += s[p]
                p += 1
            result.append(string)
        return result