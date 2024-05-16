import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev_nums = [-i for i in nums]
        heapq.heapify(rev_nums)
        ctr = 0
        while ctr < k:
            elt = heapq.heappop(rev_nums)
            ctr += 1
        return -elt  
