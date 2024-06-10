# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        # def min_helper(root, curr_min = None):
        #     if not curr_min:
        #         curr_min = float("inf")
        #     if not root:
        #         return curr_min
        #     elif not root.left and not root.right:
        #         return curr_min
        #     elif root.left and not root.right:
        #         return min(root.val - root.left.val, min_helper(root.left, curr_min))
        #     elif root.right and not root.left:
        #         return min(root.right.val - root.val, min_helper(root.right, curr_min))
        #     else:
        #         return min(root.val - root.left.val, min_helper(root.left, curr_min), root.right.val - root.val, min_helper(root.right, curr_min))

        # return min_helper(root)

        self.min_diff = float("inf")
        self.prev = float("-inf")

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev != float("-inf"):
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff
