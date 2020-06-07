# 373. Find K Pairs with Smallest Sums


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k:
            return []

        heap = []
        for u in nums1:
            for v in nums2:
                heappush(heap, (u + v, [u, v]))  # keeping [u, v] for later

        result = []
        for i in range(k):
            if len(heap):
                sum, pair = heappop(heap)
                result.append(pair)

        return result
