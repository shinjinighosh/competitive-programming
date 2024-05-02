class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res = [0, 0]
        curr = 0
        for num in nums1:
            if num in nums2_set:
                curr += 1
        res[0] = curr
        curr = 0
        for num in nums2:
            if num in nums1_set:
                curr += 1
        res[1] = curr
        return res

