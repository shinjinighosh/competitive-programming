class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        stack1 = nums1[:m][::-1]
        stack2 = nums2[::-1]
        res = []
        while stack1 and stack2:
            peek1 = stack1[-1]
            peek2 = stack2[-1]
            if peek1 <= peek2:
                res.append(stack1.pop())
            else:
                res.append(stack2.pop())
        if stack1:
            while stack1:
                res.append(stack1.pop())
        elif stack2:
            while stack2:
                res.append(stack2.pop())
        for i in range(len(res)):
            nums1[i] = res[i]
        


        
