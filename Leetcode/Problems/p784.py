# 784. Letter Case Permutation

'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
'''


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # return list(set(self.gen(S)))
        S = [i for i in S]
        self.ans = []
        self.backtrack(S, 0)
        return self.ans

    # def gen(self, s):
    #     if not s:
    #         return ""
    #     if len(s) == 1:
    #         if s.isnumeric():
    #             yield s
    #         else:
    #             yield s.lower() if s.isupper() else s.upper()
    #             yield s
    #     else:
    #         for i in range(len(s)-1):
    #             for op in list(self.gen(s[i])):
    #                 for headop in list(self.gen(s[:i])):
    #                     for tailop in list(self.gen(s[i+1:])):
    #                         # yield s[:i] + op + s[i+1:]
    #                         yield headop + op + tailop
    #         if not s:
    #             return ""
    #         else:
    #             for op in self.gen(s[-1]):
    #                 for headop in list(self.gen(s[:-1])):
    #                 # yield s[:-1] + op
    #                     yield headop + op
    def backtrack(self, A, index):
        if index == len(A):
            self.ans.append("".join(A))
            return

        if A[index].isalpha():
            A[index] = A[index].lower()
            self.backtrack(A, index + 1)
            A[index] = A[index].upper()
            self.backtrack(A, index + 1)
        else:
            self.backtrack(A, index + 1)
