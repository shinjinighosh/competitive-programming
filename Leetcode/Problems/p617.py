# 617. Merge Two Binary Trees

'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        res = TreeNode()
        if not t1 and not t2:
            return t1
        elif not t2:
            res.val = t1.val
            if t1.left:
                res.left = t1.left
            if t1.right:
                res.right = t1.right
            return res
        elif not t1:
            res.val = t2.val
            if t2.right:
                res.right = t2.right
            if t2.left:
                res.left = t2.left
            return res
        else:  # both t1 and t2 exist
            res.val = t1.val + t2.val
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
            return res
