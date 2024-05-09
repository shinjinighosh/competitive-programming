class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness.sort()
        # greedy solution, accounting for the fact that in the i-th turn, each child's happiness value
        # has already been decreased by i
        for i in range(k):
            res += max(happiness.pop() - i, 0)
        return res
        
