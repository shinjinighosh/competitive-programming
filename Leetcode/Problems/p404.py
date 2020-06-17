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
        if not root:
            return 0
        elif not root.left and not root.right:
            return 0
        elif root.left and not root.right:
            if not root.left.left and not root.left.right:
                return root.left.val
            else:
                return self.sumOfLeftLeaves(root.left)
        elif root.right and not root.left:
            return self.sumOfLeftLeaves(root.right)
        else:
            if not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
