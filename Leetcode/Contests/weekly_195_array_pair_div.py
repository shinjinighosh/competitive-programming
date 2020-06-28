# 5449. Check If Array Pairs Are Divisible by k

'''
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.
'''


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modded_array = [i % k for i in arr]
        # print(modded_array)
        taken_indices = set()
        unique_vals = set(modded_array)
        counts = {}
        for i in modded_array:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        # print('counts', counts)
        for val in unique_vals:
            if val == 0:
                if counts[val] % 2 != 0:
                    return False
            elif (k - val) not in counts.keys() or counts[val] != counts[k - val]:
                return False
        return True

        # copy = modded_array.copy()
        # for i in range(len(modded_array)):
        #     first = modded_array[i]
        #     if (k-first) not in copy:
        #         return False
        #     else:
        #         idx = copy.index(k-first)
        #         # taken_indices.add()
        #         copy.pop(copy.index(first))
        #         copy.pop(idx)
        # return True
