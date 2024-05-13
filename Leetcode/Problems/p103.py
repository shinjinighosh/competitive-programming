# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [(root, 0)]
        last_depth = 0
        temp = []
        while q:
            # print([(n.val, d) for n, d in q])
            # print(temp)
            node, depth = q.pop(0)
            if depth != last_depth:
                if last_depth % 2 == 0:
                    res.append(temp)
                else:
                    res.append(temp[::-1])
                temp = [node.val]
                last_depth = depth
            else:
                temp.append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
            if not q:
                if last_depth % 2 == 0:
                    res.append(temp)
                else:
                    res.append(temp[::-1])
        return res
                
        
