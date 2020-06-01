# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if not root.left and not root.right:
            return root
        else:
            if root.left and not root.right:
                root.right = self.invertTree(root.left)
                root.left = None
                return root
            elif root.right and not root.left:
                root.left = self.invertTree(root.right)
                root.right = None
                return root
            else:
                root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
                return root
