# 5188. Kth Ancestor of a Tree Node

'''
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.
'''


class TreeAncestor:

    def __init__(self, n, parent):
        self.n = n
        self.tree = parent
        self.dict = {i: parent[i] for i in range(len(parent))}
        pass

    def getKthAncestor(self, node, k):
        # if k > self.n:
        # return -1
        if k == 0:
            return node
        current = node
        while k > 0:
            try:
                current = self.dict[current]
                if current == -1:  # reached root
                    return -1
                k -= 1
                if k == 0:
                    return current
            except:
                return -1
        return -1


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
# should be 1, 0, -1
print(treeAncestor.getKthAncestor(3, 1))
print(treeAncestor.getKthAncestor(5, 2))
print(treeAncestor.getKthAncestor(6, 3))
