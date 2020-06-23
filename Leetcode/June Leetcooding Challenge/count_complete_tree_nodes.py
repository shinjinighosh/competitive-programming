#   Count Complete Tree Nodes

'''
Given a complete binary tree, count the number of nodes.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root and not root.left and not root.right:
            return 1
        elif root and root.right and not root.left:
            return 1 + self.countNodes(root.right)
        elif root and root.left and not root.right:
            return 1 + self.countNodes(root.left)
        else:  # has both sides
            return 1 + self.countNodes(root.right) + self.countNodes(root.left)

    # Alternate shorter solution
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     else:
    #         return 1 + self.countNodes(root.right) + self.countNodes(root.left)
