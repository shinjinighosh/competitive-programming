class Solution:
    def numSteps(self, s: str) -> int:
        # n = int(s, 2)
        # steps = 0
        # while n != 1:
        #     steps += 1
        #     if n % 2 == 0:
        #         n = int(n/2)
        #     else:
        #         n += 1
        # return steps

        steps = 0
        while s != "1":
            if s[-1] == "0": # even
                s = s[:-1] # removing the last digit is the same as dividing by 2
            else:
                i = len(s) - 1
                while i >= 0 and s[i] == "1":
                    i -= 1
                if i == -1: # all ones
                    s = "1" + "0" * len(s)
                else:
                    # flip the first '0' from the right to '1' and all '1's to its right to '0's
                    s = s[:i] + "1" + "0" * (len(s) - i - 1)
            steps += 1
        return steps
