# 102. Binary Tree Level Order Traversal

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
            if node.left:
                q.append((node.left, depth + 1,))
            if node.right:
                q.append((node.right, depth + 1,))
        return node_vals
