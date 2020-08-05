# 22. Generate Parentheses

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def helper(s, n, result, numOpening, numClosing):
            if len(s) == n * 2:
                result.append(s)
                return

            #candidates = ["(",")"]
            if numOpening < n:
                helper(s + "(", n, result, numOpening + 1, numClosing)
            if numClosing < numOpening:
                helper(s + ")", n, result, numOpening, numClosing + 1)
            if not n:
                return [""]

        result = []
        s = "("
        numOpening = 1
        numClosing = 0
        helper(s, n, result, numOpening, numClosing)
        return result
