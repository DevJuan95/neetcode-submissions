class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i+=1
            size = int(size)
            i+=1
            word = s[i:i+size]
            print(size,word)
            res.append(word)
            i+=size
        return res