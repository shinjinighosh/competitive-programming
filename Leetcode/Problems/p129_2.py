# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # this wrongly calculates the sum of all posible paths from root to leaf
        # def helper(root, curr_sum):
        #     if not root:
        #         return curr_sum
        #     elif not root.left and not root.right:
        #         return root.val + curr_sum
        #     elif root.left and not root.right:
        #         return helper(root.left, curr_sum + root.val) # + root.val + curr_sum
        #     elif root.right and not root.left:
        #         return helper(root.right, curr_sum + root.val) # + root.val + curr_sum
        #     else:
        #         return helper(root.left, curr_sum + root.val) + helper(root.right, curr_sum + root.val) # + root.val + curr_sum
        
        # return helper(root, 0)
        
        # cascade down to make each leaf's value the path till then, and then return the sum of all leaves
        if not root:
            return 0
        elif not root.left and not root.right:
            return int(root.val)
        if root.left:
            root.left.val += 10 * root.val
        if root.right:
            root.right.val += 10 * root.val
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)


