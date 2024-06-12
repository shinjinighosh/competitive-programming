class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # freq = {0:0, 1:0, 2:0}
        # for i in nums:
        #     freq[i] += 1
        # print(nums)
        # nums = [0] * freq[0] + [1] * freq[1] + [2] * freq[2]
        # nums =  [0 for _ in range(freq[0])] + [1 for _ in range(freq[1])] + [2 for _ in range(freq[2])]
        # print(nums)
        # i = 0
        # j = 0
        # k = 0
        # for i in range(freq[0]):
        #     nums[i] = 0
        # # start = 
        # for j in range(i+1, i + freq[1]+1):
        #     nums[j] = 1
        # for k in range(j+1, j + freq[2]+1):
        #     nums[k] = 2
        # for i in range(len(nums)):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
            
