# 5185. Three Consecutive Odds

'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # arr.sort()
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                # diff = arr[i+1] - arr[i]
                # if arr[i+2] - arr[i+1] == diff:
                return True
        return False
