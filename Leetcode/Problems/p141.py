# check for cycle in Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        all_nodes = set()
        while head:
            if head in all_nodes:
                return True
            all_nodes.add(head)
            head = head.next
        return False
