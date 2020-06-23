# 654. Maximum Binary Tree

'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return TreeNode()
        root_val = max(nums)
        res = TreeNode(root_val)
        max_idx = nums.index(root_val)
        if nums[:max_idx]:
            left_tree = self.constructMaximumBinaryTree(nums[:max_idx])
            res.left = left_tree
        if len(nums) > max_idx and nums[max_idx + 1:]:
            right_tree = self.constructMaximumBinaryTree(nums[max_idx + 1:])
            res.right = right_tree
        return res
