class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = [1, 2]
        idx = 2
        while idx <= n:
            # you can either take one step from where you were last, or two steps from the place before that
            num_steps.append(num_steps[idx-1] + num_steps[idx-2])
            idx += 1
        return num_steps[n-1]
