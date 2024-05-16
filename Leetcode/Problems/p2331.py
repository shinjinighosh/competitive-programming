# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif not root.left and not root.right: # leaf node
            return root.val
        else: # it is full so it will always have both left and right
            if root.val == 2: 
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            else: 
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
