class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for char in s:
            if idx >= len(t):
                return False # reached end of t
            while t[idx] != char:
                idx += 1
                if idx >= len(t):
                    return False # reached end of t
            if t[idx] == char:
                idx += 1
        return True
               
            
            # if char not in t[idx:]:
            #     return False
            # else:
            #     if idx > len(t):
            #         return False
            #     else:
            #         idx += t[idx:].index(char) 
        # return True
    
