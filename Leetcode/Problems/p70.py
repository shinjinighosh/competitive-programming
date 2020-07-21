# 70. Climbing Stairs

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = [1, 2]
        counter = 2
        while counter <= n:
            one_step = num_steps[counter - 1]
            two_steps = num_steps[counter - 2]
            num_steps.append(one_step + two_steps)
            counter += 1
        return num_steps[n - 1]
