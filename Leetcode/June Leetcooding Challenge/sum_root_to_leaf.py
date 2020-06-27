#   Sum Root to Leaf Numbers

'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return int(root.val)
        if root.left:
            root.left.val = 10 * root.val + root.left.val
        if root.right:
            root.right.val = 10 * root.val + root.right.val
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)

        # def getPaths(root, res=None):
        #     if not res:
        #         res = []
        #     if not root.left and not root.right:
        #         return res
        #     elif not root.left:  # only right side exists
        #         if res:
        #             temp = res[-1]
        #         else:
        #             temp = []
        #         res.append(temp + [self.val])
        #
        # def getPaths(root, res=None):
        #     if not res:
        #         res = []
        #     if not root:
        #         return res
        #     elif not root.left and not root.right:
        #         res.append(res.pop() + root.val)
        #         return res
        #     elif not root.left:  # only right side exists
        #         right_sum = getPaths(root.right)
        #         res.append(res.pop() + root.val + right_sum)
        #     elif not root.left:  # only left side exists
        #         left_sum = getPaths(root.left)
        #         res.append(res.pop() + root.val + left_sum)
        #     else:
        #         left_sum = getPaths(root.left)
        #         right_sum = getPaths(root.right)
        #         current_sum = res.pop()
        #         res.append(current_sum + root.val + left_sum)
        #         res.append(current_sum + root.val + right_sum)
        #         return res return get
