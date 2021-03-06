# 590. N-ary Tree Postorder Traversal

'''
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        if not root.children:
            res.append(root.val)
            return res
        else:
            for child in root.children:
                res.extend(self.postorder(child))
            res.append(root.val)
            return res
