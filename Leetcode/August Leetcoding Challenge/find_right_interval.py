# Find Right Interval

'''
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
'''


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        int_to_idx = {}
        for idx, interval in enumerate(intervals):
            int_to_idx[tuple(sorted(interval))] = idx
        sorted_int = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(sorted_int)
        res = [-1 for _ in range(len(intervals))]
        for i in range(len(sorted_int) - 1):
            interval = sorted_int[i]
            pos = int_to_idx[tuple(sorted(interval))]
            next_pos = -1
            for j in range(i + 1, len(sorted_int)):
                next_int = sorted_int[j]
                # print(next_int, interval)
                if next_int[0] >= interval[1]:
                    next_pos = int_to_idx[tuple(sorted(next_int))]
                    break
            res[pos] = next_pos
        return res
