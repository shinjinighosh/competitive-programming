class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1]) # sort by endpoints
        # greedy solution where you start with bursting the end of balloon one, count how many it overlapped with, and move on
        count = 0
        idx = 0
        overlapping = lambda x, start, end: start <= x <= end
        while idx < len(points):
            chosen = points[idx][1]
            count += 1
            idx += 1
            while idx < len(points) and overlapping(chosen, points[idx][0], points[idx][1]):
                idx += 1 # these balloons are also burst by the same arrow
            # if not, need a new arrow
        return count

