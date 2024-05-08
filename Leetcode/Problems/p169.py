class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) % 2 == 0:
            trigger = len(nums) / 2
        else:
            trigger = int(len(nums)/2) + 1
        # trigger = round(len(nums)/2)
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
                if freq[i] >= trigger:
                    return i
            else:
                freq[i] = 1
        return i
