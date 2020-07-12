# 1386. Cinema Seat Allocation

'''
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.
'''


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        # slow solution
        # groups = 0
        # reserved = set()
        # for seat in reservedSeats:
        #     reserved.add(tuple(seat))
        # for row in range(1, n+1):
        #     left = [(row,2), (row,3), (row,4), (row,5)]
        #     right = [(row,6), (row,7), (row,8), (row,9)]
        #     middle = [(row,4), (row,5), (row,6), (row,7)]
        #     l = all([i not in reserved for i in left])
        #     r = all([i not in reserved for i in right])
        #     if l and r:
        #         groups += 2
        #     elif l or r:
        #         groups += 1
        #     elif all([i not in reserved for i in middle]):
        #         groups += 1
        # return groups

        res = 2 * n
        rows = collections.defaultdict(set)
        for r, c in reservedSeats:
            rows[r].add(c)

        middle = {2, 3, 4, 5, 6, 7, 8, 9}
        left = {2, 3, 4, 5}
        right = {6, 7, 8, 9}
        small_middle = {4, 5, 6, 7}

        for r in rows:
            reserved = rows[r]
            # 2 choices
            if len(reserved & middle) == 0:
                continue
            # 1 choice
            elif len(reserved & left) == 0 or len(reserved & right) == 0 or len(reserved & small_middle) == 0:
                res -= 1
            # 0 choice
            else:
                res -= 2
        return res
