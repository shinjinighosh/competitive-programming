# 515. Find Largest Value in Each Tree Row

'''
You need to find the largest value in each row of a binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        current_maxes = {}
        # bfs and store depth
        q = [(root, 0)]
        num_levels = 0
        while q:
            node, depth = q.pop(0)
            if depth not in current_maxes or node.val > current_maxes[depth]:
                current_maxes[depth] = node.val
            if node.right:
                q.append((node.right, depth + 1))
                num_levels = depth + 1
            if node.left:
                q.append((node.left, depth + 1))
                num_levels = depth + 1
        # num_levels = max(current_maxes.keys()) # if not changing every time
        for level in range(num_levels + 1):
            res.append(current_maxes[level])
        return res
