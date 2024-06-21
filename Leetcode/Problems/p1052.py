class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        grump_totals = [a * b for a, b in zip(customers, grumpy)]
        if minutes >= len(grumpy):
            return sum(customers)
        if minutes == 0:
            return sum(grump_totals)
        # print(grump_totals)
        cands = [sum(grump_totals[:minutes])]
        max_grump = cands[0]
        max_grump_start_idx = 0
        for i in range(minutes, len(grump_totals)):
            # print(i, cands)
            new_sum = cands[-1] - grump_totals[i - minutes] + grump_totals[i]
            cands.append(new_sum)
            if new_sum > max_grump:
                max_grump = new_sum
                max_grump_start_idx = i - minutes + 1 # that is where the window starts
        # print(cands, max_grump, max_grump_start_idx)
        res = 0
        for idx, (a, b) in enumerate(zip(customers, grumpy)):
            if max_grump_start_idx <= idx < max_grump_start_idx + minutes: # he is not grumpy, used his secret
                res += a
            else:
                res += a * (1 - b)
        return res


