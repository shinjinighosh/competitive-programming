# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_last_node(self, root):
        # get the last node of a flat "tree" aka linked list
        while root.right:
            root = root.right
        return root
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        elif not root.left and not root.right:
            return
        elif root.left and not root.right:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            return
        elif root.right and not root.left:
            self.flatten(root.right)
            return
        else:
            # both left and right exist
            self.flatten(root.left)
            self.flatten(root.right)
            self.get_last_node(root.left).right = root.right
            root.right = root.left
            root.left = None
            return

