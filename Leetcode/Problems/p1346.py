# 1346. Check If N and Its Double Exist

'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
'''


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in arr:
            if (i % 2 == 0 and i // 2 in seen) or (i * 2 in seen):
                return True
            seen.add(i)
        return False
