'''
Creating a list representation of a min-heap

1. Understand
[1, 2, 3, 4, 5]

insert(6) --> [1,2,3,4,5,6]
insert(0) --> [0,1,2,3,4,5,6]

2. Match
parent = (current_index - 1) // 2
left child = (current_index * 2) + 1
right child = (current_index * 2) + 2
bubbling up insert - add to end of list, compare with parent and swap if necessary

3. PseudoCode

MinHeap Class

@param list
@return None, stores array
__init __
  if given a list
    start with []
    for each elt in list
      insert()

get_parent(idx)
  parent = (current_index - 1) // 2
get_left_child(idx)
  left child = (current_index * 2) + 1
get_right_child(idx)
  right child = (current_index * 2) + 2

insert(value)
  add to end
  while parent > value
    swap with parent

'''


class MinHeap:
    def __init__(self, array=[]):
        self.heap = []
        for n in array:
            self.insert(n)

    def get_parent(self, idx):
        return (idx - 1) // 2

    def get_left_child(self, idx):
        return (idx * 2) + 1

    def get_right_child(self, idx):
        return (idx * 2) + 2

    # O(log n)
    def insert(self, n):
        self.heap.append(n)
        cur_idx = len(self.heap) - 1
        parent_idx = self.get_parent(cur_idx)
        while parent_idx >= 0 and self.heap[parent_idx] > n:
            self.heap[cur_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[cur_idx]
            cur_idx = parent_idx
            parent_idx = self.get_parent(cur_idx)


min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(4)
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(1)

print(min_heap.heap)
