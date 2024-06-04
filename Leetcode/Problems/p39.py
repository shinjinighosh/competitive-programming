class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(rem, combo, start):
            if rem == 0:
                res.append(list(combo))
                return
            elif rem < 0:
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(rem - candidates[i], combo, i)
                combo.pop()

        res = []
        backtrack(target, [], 0)
        return res
