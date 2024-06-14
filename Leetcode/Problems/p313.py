class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # ugly = [1]
        # heap = []
        # seen = set([1])

        # for prime in primes:
        #     heapq.heappush(heap, (prime, 0)) # value, index
        
        # while len(ugly) < n:

        #     val, idx = heapq.heappop(heap)

        #     if val > ugly[-1]:
        #         ugly.append(val)
            
        #     for prime in primes:
        #         next_val = prime * ugly[idx + 1]
        #         if next_val not in seen:
        #             seen.add(next_val)
        #             heapq.heappush(heap, (next_val, idx + 1))

        # return ugly[-1]

        ugly = [1] * n  # array to store the first n super ugly numbers
        idx = [0] * len(primes)  # indices for each of the primes
        values = primes[:]  # current value of prime multiples
        
        for i in range(1, n):
            # Find the next minimum value from the current values
            next_val = min(values)
            ugly[i] = next_val
            
            # Update the indices and values for the next round
            for j in range(len(primes)):
                if values[j] == next_val:
                    idx[j] += 1  # move pointer for this prime
                    values[j] = ugly[idx[j]] * primes[j]  # calculate the new value for this prime
        
        return ugly[-1]

