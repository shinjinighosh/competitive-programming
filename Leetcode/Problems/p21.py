# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        while list1 or list2:
            elt1 = list1.val if list1 else float("inf")
            elt2 = list2.val if list2 else float("inf")
            if elt1 < elt2:
                curr.next = ListNode(elt1)
                list1 = list1.next
            elif elt2 < elt1:
                curr.next = ListNode(elt2)
                list2 = list2.next
            else:
                curr.next = ListNode(elt1)
                curr = curr.next
                curr.next = ListNode(elt2)
                list1 = list1.next
                list2 = list2.next
            curr = curr.next
        return res.next

