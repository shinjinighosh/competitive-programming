# 987. Vertical Order Traversal of a Binary Tree

'''
Print a Binary Tree in Vertical Order

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively
will be at positions (X-1, Y-1) and (X+1, Y-1).

Return a list of lists of the elements in each vertical level, from left to right
and top to bottom in each list.

          1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9

The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.


The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

pseudocode:
--> some traversal of tree (bfs)
--> map node_value -> position tuple(x,y)
--> for all same y's --> sort node_values first by x_value, tiebreak by node_value
--> return list[list] format

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # def verticalOrder(root: TreeNode) -> list(list(int)):
        q = [(root, (0, 0,))]
        node_position_map = {}

        while q:
            node, position = q.pop(0)
            node_position_map[root.val] = position
            x_map[position[0]].append(root.val)
            if node.left:
                q.append((node.left, (position[0] - 1, position[1] - 1)))
                # node_position_map[root.left.val]
            if node.right:
                q.append((node.right, (position[0] + 1, position[1] - 1)))

        x_mapping = {}  # x_value:[(node_val,y_value)]
        x_vals = []

        # {0: [1,5,6,], ....}
        for node_value, pos in node_position_map:
            x, y = pos
            if x not in x_value:
                x_vals.append(x)
                x_mapping[x] = [(node_value, y)]
            else:
                x_mapping[x].append((node_value, y))

        x_vals.sort()
        res = []

        for x in x_vals:
            vals = [i[0] for i in x_mapping[x]]
            vals.sort(key=lambda x: (1 / node_position_map[x][1], x))
            res.append(vals)

        return res
