# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        memo = {value: idx for idx, value in enumerate(inorder)}

        def array_to_tree(left, right):
            nonlocal preorder_idx
            if left > right:
                return None

            root_value = preorder[preorder_idx]
            root = TreeNode(root_value)

            idx = memo[root_value]
            preorder_idx += 1

            root.left = array_to_tree(left, idx - 1)
            root.right = array_to_tree(idx + 1, right)

            return root

        preorder_idx = 0
        return array_to_tree(0, len(inorder)-1)
