class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= current_max:
                res.append(True)
            else:
                res.append(False)
        return res
