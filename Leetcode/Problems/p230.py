# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.counter = 0

        def inorder(node):
            if not node or self.counter >= k:
                return
            inorder(node.left)

            self.counter += 1
            if self.counter == k:
                self.res = node.val
                return
            inorder(node.right)

        self.res = -1
        inorder(root)
        return self.res

        
