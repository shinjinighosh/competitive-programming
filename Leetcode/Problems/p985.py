# 985. Sum of Even Numbers After Queries

'''
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
'''


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s = sum([i for i in A if i % 2 == 0])
        for val, idx in queries:
            if A[idx] % 2 == 0:
                s -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                s += A[idx]
            res.append(s)
        return res
