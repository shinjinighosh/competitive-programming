"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # commented code would work if it were an adj list
        # new_nodes = {} # node val: node object (reference by val)
        # if not node:
        #     return []
        # for idx, neighbors in enumerate(node):
        #     curr_node_val = idx + 1
        #     curr_node_neighbors = []
        #     for neighbor_val in neighbors:
        #         if neighbor_val in new_nodes:
        #             curr_node_neighbors.append(new_nodes[neighbor_val])
        #         else:
        #             new_nodes[neighbor_val] = Node(neighbor_val)
        #             curr_node_neighbors.append(new_nodes[neighbor_val])
        #     if curr_node_val in new_nodes:
        #         new_nodes[curr_node_val].neighbors = curr_node_neighbors
        #     else:
        #         new_nodes[curr_node_val] = None(curr_node_val, curr_node_neighbors)

        # all_keys = sorted(new_nodes.keys())
        # res = []
        # for key in all_keys:
        #     res.append(new_nodes[key].neighbors)
        # return res

        if not node:
            return None
        
        new_nodes = {} # node val: node object (reference by val)
        new_head = Node(1)
        new_nodes[1] = new_head

        agenda = [node]
        seen = set()
        while agenda:
            head = agenda.pop(0)
            if head.val in seen:
                continue
            seen.add(head.val)
            for neighbor in head.neighbors:
                if neighbor.val in new_nodes:
                    new_nodes[head.val].neighbors.append(new_nodes[neighbor.val])
                else:
                    new_nodes[neighbor.val] = Node(neighbor.val)
                    new_nodes[head.val].neighbors.append(new_nodes[neighbor.val])
                if neighbor.val not in seen:
                    agenda.append(neighbor)
        return new_head



        
