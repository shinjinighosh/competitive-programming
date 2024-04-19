class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        def leftSum(arr):
            res = [0]
            for num in arr[:-1]:
                res.append(res[-1] + num)
            return res
        def rightSum(arr):
            res = [0]
            for num in arr[::-1][:-1]:
                res.append(res[-1] + num)
            return res [::-1]

        return list(map(lambda pair: abs(pair[0] - pair[1]), zip(leftSum(nums), rightSum(nums))))


