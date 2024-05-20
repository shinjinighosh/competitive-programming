class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        t_ptr = 0

        if not s:
            return True
        elif not t:
            return False

        while t:
            curr_s = s[s_ptr]
            curr_t = t[t_ptr]
            if curr_s == curr_t:
                s_ptr += 1
                t_ptr += 1
                if s_ptr == len(s):
                    return True # have reached the end of s
            else:
                t_ptr += 1
            
            if t_ptr >= len(t):
                return False # exhausted t 
        
        return False
