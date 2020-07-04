# 1299. Replace Elements with Greatest Element on Right Side

'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [i for i in arr]
        res[-1] = -1
        running_max = -1
        if len(arr) == 1:
            return res
        for i in range(len(arr) - 2, -1, -1):
            if arr[i + 1] > running_max:
                running_max = arr[i + 1]
            # res[i] = max(running_max, arr[i+1])
            res[i] = running_max
        return res
