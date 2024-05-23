class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        result = []
        
        # Map to store numbers and fast check if number+k or number-k exists
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        
        def isBeautiful(subset):
            # Check the current subset for any pairs that differ by k
            seen = set()
            for num in subset:
                if (num + k) in seen or (num - k) in seen:
                    return False
                seen.add(num)
            return True
        
        def backtrack(start, path):
            if path and isBeautiful(path):
                result.append(path[:])  # Store a copy of the current path if it's a valid subset
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return len(result)

