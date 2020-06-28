# 1491. Average Salary Excluding the Minimum and Maximum Salary

'''
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.
'''


class Solution:
    def average(self, salary: List[int]) -> float:
        c = 0
        s = 0
        maximum = max(salary)
        minimum = min(salary)
        if maximum == minimum:
            sub = 1
        else:
            sub = 2
        return sum([num for num in salary if num != maximum and num != minimum]) / (len(salary) - sub)
