# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root
        else:
            agenda = deque([(root, 1)])
            while agenda:
                curr_node, curr_depth = agenda.popleft()
                if curr_depth == depth - 1:
                    new_left = TreeNode(val, curr_node.left)
                    new_right = TreeNode(val, None, curr_node.right)
                    curr_node.left = new_left
                    curr_node.right = new_right
                    # no need to go further down the depth on this side
                else:
                    if curr_node.left:
                        agenda.append((curr_node.left, curr_depth + 1))
                    if curr_node.right:
                        agenda.append((curr_node.right, curr_depth + 1))
            return root
