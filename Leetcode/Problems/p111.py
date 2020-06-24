# 111. Minimum Depth of Binary Tree

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return 1 + self.minDepth(root.left)
        elif root.right and not root.left:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
