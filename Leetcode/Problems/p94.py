# 94. Binary Tree Inorder Traversal

'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        if not root.right and not root.left:
            res.append(root.val)
            return res
        else:
            if root.left:
                res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            if root.right:
                res.extend(self.inorderTraversal(root.right))
            return res
