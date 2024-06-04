# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = defaultdict() # maps level to rightmost node on that level
        agenda = deque([(root, 0)])
        while agenda:
            curr_node, curr_level = agenda.popleft()
            if not curr_node:
                return res
            res[curr_level] = curr_node.val
            if curr_node.left:
                agenda.append((curr_node.left, curr_level + 1))
            if curr_node.right:
                agenda.append((curr_node.right, curr_level + 1))
        return res.values()
