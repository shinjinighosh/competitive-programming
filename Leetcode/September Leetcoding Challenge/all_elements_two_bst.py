# All Elements in Two Binary Search Trees

'''
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def traverse(root, res):
            if not root:
                return res
            else:
                res.append(root.val)
            # if root and not root.right and not root.left:
            #     res.append(root.val)
            #     return res
            # else:
                res = traverse(root.left, res)
                res = traverse(root.right, res)
                return res
        res1 = traverse(root1, [])
        res2 = traverse(root2, [])
        res = res1 + res2
        res.sort()
        return res
