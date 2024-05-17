# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def rev(root, end): # reverse the list from root to end
            res = ListNode()
            curr = res
            
            return res.next


        res = ListNode()
        curr = res
        while head.val != left:
            curr.next = ListNode(head.val)
            curr = curr.next
            head = head.next
        # we have approached left
        reversed_list_head = rev(head, end)
        curr.next = reversed_list_head
        while curr.next:
            curr = curr.next
        while head:
            curr.next = ListNode(head.val)
            head = head.next
            curr = curr.next
        return res.next

