# 5468. Kth Missing Positive Number

'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missings = []
        curr = 1
        i = 0
        while i < len(arr):
            if arr[i] == curr:
                curr += 1
                i += 1
            else:
                missings.append(curr)
                curr += 1
        missings.append(curr)
        if len(missings) >= k:
            return missings[k - 1]
        return missings[-1] + (k - len(missings))
