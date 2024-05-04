# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        res = ListNode()
        curr = res
        carry = 0
        a = l1
        b = l2

        while a or b:
            d1 = a.val if a else 0
            d2 = b.val if b else 0
            digit = (d1 + d2 + carry) % 10
            carry = (d1 + d2 + carry) // 10
            curr.next = ListNode(digit)
            curr = curr.next
            if a:
                a = a.next
            if b:
                b = b.next
        if carry:
            curr.next = ListNode(carry)
        return res.next

