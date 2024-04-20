class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # greedy should suffice

        # is_bal = lambda x: x.count("L") == x.count("R")
        counter = 0
        curr_counter = 0
        for l in s:

            if l == "L":
                curr_counter += 1
            elif l == "R":
                curr_counter -= 1

            if curr_counter == 0: # end of a balanced string, start of another
                counter += 1
        
        return counter
        
