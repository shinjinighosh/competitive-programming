class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        res = nums[::-1]
        res[:k] = res[:k][::-1]
        res[k:] = res[k:][::-1]
        for idx, num in enumerate(res):
            nums[idx] = res[idx]
