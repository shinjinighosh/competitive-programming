# 653. Two Sum IV - Input is a BST

'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        q = [root]
        while q:
            node = q.pop(0)
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return False
