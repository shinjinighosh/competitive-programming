# 1507. Reformat Date

'''
Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
'''


class Solution:
    def reformatDate(self, date: str) -> str:
        l = date.split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_format = months.index(l[1])
        mm = str(month_format + 1)
        if month_format < 9:
            mm = "0" + mm
        dd = l[0].rstrip("stndrh")
        if len(dd) < 2:
            dd = "0" + dd
        return (l[2] + "-" + mm + "-" + dd)
