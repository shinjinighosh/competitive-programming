# 1266. Minimum Time Visiting All Points

'''
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
'''


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            x_diff = abs(points[i][0] - points[i + 1][0])
            y_diff = abs(points[i][1] - points[i + 1][1])
            time_taken = max(x_diff, y_diff)
            # print(time_taken)
            res += time_taken
        return res
