# 746. Min Cost Climbing Stairs

'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # assumed reverse dir of stairs
        # min_costs = [cost[0], cost[1]]
        # ptr = 2
        # while ptr < len(cost):
        #     one_step = cost[ptr - 1]
        #     two_steps = cost[ptr - 2]
        #     min_costs.append(min(one_step, two_steps))
        #     ptr += 1
        # print(min_costs)
        # return min_costs[-1]

        cost = cost[::-1]
        p1 = 0
        p2 = 0
        for i in cost:
            p1, p2 = i + min(p1, p2), p1
        return min(p1, p2)
