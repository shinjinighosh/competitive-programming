# Construct Binary Tree from Inorder and Postorder Traversal

'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(post_beg, post_end, in_beg, in_end):
            if post_end - post_beg <= 0:
                return None
            ind = dic[postorder[post_end - 1]]

            root = TreeNode(inorder[ind])
            root.left = helper(post_beg, post_beg + ind - in_beg, in_beg, ind)
            root.right = helper(post_end - in_end + ind, post_end - 1, ind + 1, in_end)
            return root

        dic = {elem: it for it, elem in enumerate(inorder)}
        return helper(0, len(postorder), 0, len(inorder))
