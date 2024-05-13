# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        memo = defaultdict(list)
        q = [(root, 0,)]
        while q:
            node, level = q.pop(0)
            memo[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1, ))
            if node.right:
                q.append((node.right, level + 1, ))
        max_level = max(memo.keys())
        for i in range(max_level+1):
            res.append(memo[i])
        return res
