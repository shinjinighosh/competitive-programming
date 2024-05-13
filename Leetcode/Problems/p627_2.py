# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [(root, 0,)] # will hold (num, level)
        node_vals = [] # list of lists
        while q:
            # get the next element from the agenda
            node, level = q.pop(0)
            # store its value correctly
            if len(node_vals) < level + 1:
                node_vals.append([node.val])
            else:
                node_vals[level].append(node.val)
            # expand the agenda
            if node.left:
                q.append((node.left, level + 1,))
            if node.right:
                q.append((node.right, level + 1,))
        res = [sum(level) / len(level) for level in node_vals]
        return res

