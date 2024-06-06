# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def get_height(root):
            if not root:
                return 0
            return 1 + max(get_height(root.left), get_height(root.right))


        height = get_height(root) - 1
        m = height + 1
        n = 2 **(height + 1)  - 1

        res = [["" for i in range(n)] for j in range(m)]
        if not root:
            return res
        agenda = deque([(root, 0, int((n-1)/2))])
        while agenda:
            curr_node, r, c = agenda.popleft()
            res[r][c] = str(curr_node.val)
            if curr_node.left:
                agenda.append((curr_node.left, r + 1, c - 2 ** (height - r - 1)))
            if curr_node.right:
                agenda.append((curr_node.right, r + 1, c + 2 ** (height - r - 1)))
        return res


