class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(0, len(s)-1, 2):
            letter = s[i]
            num = int(s[i+1])
            res.append(letter)
            res.append(chr(ord(letter)+ num))
        if len(s) % 2 == 1:
            # one odd letter left
            res.append(s[-1])
        return "".join(res)
        
