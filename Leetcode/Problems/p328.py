# Odd even linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = []
        evens = []

        counter = 0
        while head:
            if counter % 2 == 0:
                odds.append(head.val)
            else:
                evens.append(head.val)
            counter += 1
            head = head.next

        total = odds + evens
        # print(total)
        # first_val = total.pop()
        res = ListNode()
        curr = res
        for new_val in total:
            curr.next = ListNode(new_val)
            curr = curr.next
        return res.next
