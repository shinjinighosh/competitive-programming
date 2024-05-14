class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        distinct_count = defaultdict(int)
        total_count = 0
        left = 0
        right = 0
        curr_count = 0 # num o subarrays with curr distinct elts

        while right < len(nums):
            num = nums[right]
            distinct_count[num] += 1
            if distinct_count[num] == 1: # we came across a new distinct element
                k -= 1
            if k < 0: # more than k distinct elts in curr window
                # move left pointer to fix
                distinct_count[nums[left]] -= 1
                if distinct_count[nums[left]] == 0:
                    k += 1
                left += 1
                curr_count = 0
            if k == 0: # exactly k distinct elts currently
                # keep shrinking window from the left while duplicate elements
                while distinct_count[nums[left]] > 1:
                    distinct_count[nums[left]] -= 1
                    left += 1
                    curr_count += 1
                total_count += curr_count + 1

            right += 1

        return total_count
