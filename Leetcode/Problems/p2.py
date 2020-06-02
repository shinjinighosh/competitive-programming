# Add two numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        a = l1
        b = l2
        curr = result
        carry = 0
        while a or b:
            d1 = a.val if a else 0
            d2 = b.val if b else 0
            total = d1 + d2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if a:
                a = a.next
            if b:
                b = b.next
        if carry:
            curr.next = ListNode(carry)
        return result.next
