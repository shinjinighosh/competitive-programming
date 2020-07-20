# Remove Linked List Elements

'''
Remove all elements from a linked list of integers that have value val.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # misses last
        # dummy = ListNode()
        # curr = dummy
        # while head is not None:
        #     if head.val == val:
        #         head = head.next
        #         print(head.val)
        #     else:
        #         curr.next = head
        #         curr = curr.next
        #         head = head.next
        #         print(curr.val, head.val)
        # return dummy.next

        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
