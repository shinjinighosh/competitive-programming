class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window of size k
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False
