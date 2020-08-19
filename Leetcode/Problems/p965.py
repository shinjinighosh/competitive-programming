# 965. Univalued Binary Tree

'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left:
            return root.val == root.right.val and self.isUnivalTree(root.right)
        if not root.right:
            return root.val == root.left.val and self.isUnivalTree(root.left)
        else:
            return root.val == root.right.val == root.left.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
