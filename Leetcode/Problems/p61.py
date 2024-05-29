# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        # get length first
        curr = head
        l = 1
        while curr.next:
            l += 1
            curr = curr.next
        k = k % l
        if k == 0:
            return head

        new_tail = head
        for i in range(l - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        curr.next = head

        return new_head
