# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = [(root, 0, )]
        while q:
            node, level = q.pop(0)
            if len(res) > level:
                res[level].append(node.val)
            else:
                res.append([node.val])
            if node.left:
                q.append((node.left, level +1, ))
            if node.right:
                q.append((node.right, level +1, ))
        result = []
        for idx, elt in enumerate(res):
            if idx % 2 == 0:
                result.append(elt)
            else:
                result.append(elt[::-1])
        return result
