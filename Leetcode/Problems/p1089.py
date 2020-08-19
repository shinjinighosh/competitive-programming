# 1089. Duplicate Zeros

'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        i = 0
        while len(res) < len(arr):
            if arr[i] == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(arr[i])
            i += 1
        for i in range(len(arr)):
            arr[i] = res[i]
