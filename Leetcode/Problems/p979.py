# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0 # no excess or deficit
            
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)

            curr_excess = node.val - 1 + left_excess + right_excess

            self.moves += abs(curr_excess)
            return curr_excess

        dfs(root)
        return self.moves
