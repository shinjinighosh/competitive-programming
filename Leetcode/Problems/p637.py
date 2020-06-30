# 637. Average of Levels in Binary Tree

'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
        res = []
        for level in node_vals:
            res.append(sum(level) / len(level))
        return res
