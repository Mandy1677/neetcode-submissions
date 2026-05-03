class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            currLen = len(word)
            code += str(currLen) + "#" + word
        return code
        

    def decode(self, s: str) -> List[str]:
        currLen = 0
        i = 0
        res = []
        while i < len(s):
            char = s[i]
            if char.isdigit():
                currLen = currLen * 10 + int(char)
                i += 1
            elif char == "#" and s[i-1].isdigit():
                res.append(s[i+1:i+currLen+1])
                i = i + 1 + currLen
                currLen = 0
        return res
