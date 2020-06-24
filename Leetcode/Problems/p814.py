# 814. Binary Tree Pruning

'''
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        else:
            if root.left:
                if not self.does_1_exist(root.left):
                    root.left = None
                else:
                    root.left = self.pruneTree(root.left)
            if root.right:
                if not self.does_1_exist(root.right):
                    root.right = None
                else:
                    root.right = self.pruneTree(root.right)
        return root

    def does_1_exist(self, root: TreeNode) -> bool:
        if not root:
            return False
        if root.val == 1:
            return True
        else:
            return self.does_1_exist(root.left) or self.does_1_exist(root.right)
