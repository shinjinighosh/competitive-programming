# Daily Temperatures

# correct but slow
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = []
        for i in range(len(T)):
            j = i + 1
            old = T[i]
            flag = False
            while j < len(T):
                if T[j] > T[i]:
                    res.append(j - i)
                    flag = True
                    break
                j += 1
            if not flag:  # no possible day
                res.append(0)
        return res
'''


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
