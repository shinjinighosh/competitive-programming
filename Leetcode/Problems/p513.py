# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = root.val
        curr_max_level = 0
        agenda = deque([(root, 0)])
        while agenda:
            curr_node, curr_level = agenda.popleft()
            if curr_level > curr_max_level:
                res = curr_node.val
                curr_max_level = curr_level
            if curr_node.left:
                agenda.append((curr_node.left, curr_level + 1))
            if curr_node.right:
                agenda.append((curr_node.right, curr_level + 1))
        return res
