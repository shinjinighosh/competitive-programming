# 435. Non-overlapping Intervals
'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # sorting the start times
        # if not intervals:
        #     return 0
        #
        # intervals.sort()
        #
        # end, remove = intervals[0][1], 0
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] < end: # overlap
        #         remove += 1
        #         end = min(end, intervals[i][1]) # remove the one has larger end value
        #     else:
        #         end = intervals[i][1]
        #
        # return remove

        # sorting the end times
        # count the ones we can keep
        count, end = 0, float("-inf")
        for interval in sorted(intervals, key=lambda x: x[1]):
            if end <= interval[0]:
                # print(end, interval)
                end = interval[1]
                count += 1

        return len(intervals) - count
