# 404. Sum of Left Leaves

'''
Find the sum of all left leaves in a given binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return 0
        elif not root.left and root.right:  # recurse on right side
            return self.sumOfLeftLeaves(root.right)
        elif not root.right and root.left:
            return root.left.val + self.sumOfLeftLeaves(root.left)
        elif root.left and root.right:  # both sides present
            return root.left.val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
