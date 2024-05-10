class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals [s_1, e_1] and [s_2, e_2] overlap if s_2 <= e_1
        intervals.sort(key = lambda x: x[0])
        res = []
        if not intervals:
            return res
        curr_start, curr_end = intervals[0]
        for s, e in intervals[1:]:
            if s <= curr_end:
                curr_end = max(e, curr_end)
            else:
                # finish up and sotre this interval for a new one
                res.append([curr_start, curr_end])
                curr_start, curr_end = s, e
        # for the last one
        res.append([curr_start, curr_end])
        return res
