# 429. N-ary Tree Level Order Traversal

'''
Given an n-ary tree, return the level order traversal of its nodes' values.

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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = [(root, 0,)]
        node_vals = []
        while q:
            node, depth = q.pop(0)
            if len(node_vals) < depth + 1:
                node_vals.append([node.val])
            else:
                node_vals[depth].append(node.val)
            for child in node.children:
                q.append((child, depth + 1,))
        return node_vals
