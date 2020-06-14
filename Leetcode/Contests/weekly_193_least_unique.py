# 5437. Least Number of Unique Integers after K Removals

'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

'''


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        l = list(freq.values())
        l.sort(reverse=True)
        # print(freq)
        # print(l)
        # print(k)
        while k > 0:
            if l:
                temp = l[-1]
                if temp <= k:
                    k -= temp
                    l.pop()
                    # print("popped, now l is", l, " and k is", k)
                else:
                    return len(l)
            else:
                return len(l)
        return len(l)

# s = set(arr)
# l = len(s) # num of unique elts
# if k < l: # remove one unique elt each time
#     return len(arr) - k
# else: # cannot remove more than l unique elts, will
# # return max(len(s), len(arr)-k)
#


testcase = Solution()
print(testcase.findLeastNumOfUniqueInts([5, 5, 4], 1))
print(testcase.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
