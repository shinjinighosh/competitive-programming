#   Maximum Width of Binary Tree

'''
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        level_old, num_old, max_width = 1, 1, 0
        q = [[level_old, num_old, root]]

        while q:

            [num, level, node] = q.pop(0)

            if level > level_old:
                level_old, num_old = level, num

            max_width = max(max_width, num - num_old + 1)

            if node.left:
                q.append([num * 2,  level + 1, node.left])
            if node.right:
                q.append([num * 2 + 1, level + 1, node.right])

        return max_width
