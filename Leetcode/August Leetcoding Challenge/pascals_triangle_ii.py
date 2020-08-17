# Pascal's Triangle II

'''
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.
'''


class Solution:
    def getRow(self, k: int) -> List[int]:
        return [1] + [int(str((10**10 + 1)**k)[-10 * (i + 1):-10 * i]) for i in range(1, k + 1)]
