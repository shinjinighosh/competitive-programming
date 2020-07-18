# Top K Frequent Elements
'''
Given a non-empty array of integers, return the k most frequent elements.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        topk = sorted(freq.values(), reverse=True)[:k]
        # print(topk)
        res = []
        # print(freq, topk)
        for key, val in freq.items():
            if val in topk:
                res.append(key)
        return res
