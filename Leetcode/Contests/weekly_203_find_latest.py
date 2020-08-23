# 5497. Find Latest Group of Size M

'''
Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.

At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

 '''

 # TO MAKE FASTER
 class Solution:
      def findLatestStep(self, arr: List[int], m: int) -> int:
           def getGroups(arr):
                sizes = []
                temp = 1
                for i in range(len(arr) - 1):
                    if arr[i] == "1" and arr[i] == arr[i + 1]:
                        temp += 1
                    elif arr[i] == "1":
                        sizes.append(temp)
                        temp = 1
                    elif arr[i] == "0":
                        temp = 1
                if arr[-1] == "1":
                    sizes.append(temp)
                return sizes

            s = list("0" * len(arr))
            res = -1
            for i in range(len(arr)):
                s[arr[i] - 1] = "1"
                sizes = getGroups(s)
                # print(s, sizes)
                if m in sizes:
                    res = i + 1
            return res
