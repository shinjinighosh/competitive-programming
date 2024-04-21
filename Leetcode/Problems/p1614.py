class Solution:
    def maxDepth(self, s: str) -> int:
        
        total_max = 0
        curr_max = 0

        for i in s:
            if i == "(":
                curr_max += 1
                if curr_max > total_max:
                    total_max = curr_max
            elif i == ")":
                curr_max -= 1
        
        return total_max
