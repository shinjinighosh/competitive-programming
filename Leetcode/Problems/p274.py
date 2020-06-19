# 274. H-Index

'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        if not citations:
            return 0
        l = len(citations)
        current = min(citations[0], l)
        for idx, c in enumerate(citations):
            current += max(min(c - current, l - idx - current), 0)
            if c > l - idx:
                break
        return current
