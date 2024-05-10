import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # smallest possible fraction with denominator arr[j] is arr[0] / arr[j]
        pq = [] # stores (value, num, den)
        for j in range(1, len(arr)):
            heapq.heappush(pq, (arr[0]/arr[j], 0, j))
        for ctr in range(k-1):
            elt, num, den = heapq.heappop(pq) # remove the smallest element
            # the next potential smallest fraction with the same den is arr[num+1]/arr[den], if num + 1 < den
            if num + 1 < den:
                heapq.heappush(pq, (arr[num+1]/arr[den], num+1, den))
        elt, num, den = heapq.heappop(pq)
        return [arr[num], arr[den]]

