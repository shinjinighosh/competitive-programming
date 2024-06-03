class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr_s = 0
        ptr_t = 0

        if t == s:
            return 0

        while ptr_s < len(s) and ptr_t < len(t):
            ls = s[ptr_s]
            lt = t[ptr_t]
            if ls == lt:
                ptr_s += 1
                ptr_t += 1
            else:
                ptr_s += 1

        return len(t) - ptr_t
        
                
