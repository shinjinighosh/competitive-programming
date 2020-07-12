# 455. Assign Cookies

'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.
'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        for i in range(len(g)):
            greed = g[i]
            if not s:
                break
            if s[0] >= greed:
                s.pop(0)
                content += 1
        return content
