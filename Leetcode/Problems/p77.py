# 77. Combinations

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(index, r, res):
            if len(r) == k and sorted(r) not in res:
                res.append(sorted(r))
            else:
                for i in range(index, n + 1):
                    r.append(i)
                    comb(i + 1, r, res)
                    r.pop()

        res = []
        comb(1, [], res)

        return res
