import itertools
class Solution:
    def minimumSum(self, num: int) -> int:
        # all possible pairs are all possible splits of all permutations
        digits = [int(i) for i in str(num)]
        perms = lambda x: itertools.permutations(x)

        def all_splits(inp):
            # 1234 will have [1, 234], [12, 34], [123, 4]
            res = []
            res.append([inp[0], inp[1] * 100 + inp[2] * 10 + inp[3]])
            res.append([inp[0] * 10 + inp[1], inp[2] * 10 + inp[3]])
            res.append([inp[0] * 100 + inp[1] * 10 + inp[2], inp[3]])
            return res

        get_min_of_sums = lambda lists_of_lists: min([sum(lis) for lis in lists_of_lists])

        split_pairs = [all_splits(i) for i in perms(digits)]
        return min(map(get_min_of_sums, split_pairs))
