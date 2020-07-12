# 1154. Day of the Year

'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                      6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 30}
        yy, mm, dd = date.split("-")
        yy = int(yy)
        mm = int(mm)
        dd = int(dd)
        count = 0
        if yy % 4 == 0:
            if yy % 100 != 0 or yy % 400 == 0:
                if mm >= 3:
                    count += 1
        for month in range(1, mm):
            count += month_days[month]
        count += dd
        return count
