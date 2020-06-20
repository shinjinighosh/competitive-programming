# 101. Symmetric Tree

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)


'''
NON WORKING
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

    def isSymmetric(self, root: TreeNode) -> bool:
        # dummy = root.deepcopy()
        if not root.left and not root.right:
            return True
        elif root.left and not root.right:
            return False
        elif root.right and not root.left:
            return False
        return root == self.invertTree(root)

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if not root.left and not root.right:
    #         return True
    #     elif root.left and not root.right:
    #         return False
    #     elif root.right and not root.left:
    #         return False
    #     else:
    #         if root.left.val == root.right.val:
    #             return self.isSymmetric(root.left) and self.isSymmetric(root.right)
    #         else:
    #             return False
'''
