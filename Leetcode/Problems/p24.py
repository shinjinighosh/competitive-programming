'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.


p1 p2
1  2 3 4 5
    p2 p1
2 1 3  4  5
    p1 p2
2 1 4 3 5

1
1
Two pointers
Dummy head
recursion / iterative

Check head or head.next = null -> return head
initialize a dummy head
initialize the two pointer - dummyhead.next, dummyhead.next.next
loop through the list until reaching null
  update the next pointers (swapping)
  check next.next is valid
    update pointers to next.next
return head

p1  p2
1 -> 2 -> 3 -> 4

p2  p1
2 -> 2 -> 3 -> 4

p1.next =
p2.next


       p2  p1
2   1   3   4

             d   p1 p2
             0-> 1->2-> 3->4
            -------------------------
                p2 p1
                2->1->3->4
                ^
                0 (prev)
            -------------------------
                       p1 p2
                2 ->1->3->4
                ^   ^
                0  prev
            -------------------------
                       p2     p1
                2 ->1->4->3->null
                ^         ^
                0        prev

'''


def swap_pairs(head):
    if head is None or head.next is None:
        return head
    dummy = ListNode(0)
    p1 = head
    p2 = head.next
    previous = dummy
    while p1 is not None and p2 is not None:
        # reassigning previous pointer
        previous.next = p2

        # swap
        p1.next = p2.next
        p2.next = p1

        # update pointers
        previous = p1
        p1 = p1.next
        if p1:
            p2 = p1.next
        # if p1.next.next is not None:
        #     p1 = p1.next.next
        # if p2.next.next is not None:
        #     p2 = p2.next.next
    return dummy.next
