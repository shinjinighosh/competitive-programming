#   Unique Binary Search Trees

'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
'''


class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // factorial(n) // factorial(n) // (n + 1)
