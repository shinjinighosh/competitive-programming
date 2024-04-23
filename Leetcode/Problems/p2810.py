class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for i in s:
            if i == "i":
                res = res[::-1]
            else:
                res.append(i)
        
        return "".join(res)
        
