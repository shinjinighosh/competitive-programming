class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = [] # store as list of lists
        if not nums:
            return ranges
        beginning = nums[0]
        curr = nums[0]
        for num in nums[1:]:
            if num == curr + 1:
                curr += 1
                continue
            else:
                # end that range, start a new one
                ranges.append([beginning, curr])
                beginning = num
                curr = num
        # get the ending
        ranges.append([beginning, curr])
        res = []
        for start, end in ranges:
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
        return res
