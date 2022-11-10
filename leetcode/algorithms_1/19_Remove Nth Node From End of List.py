# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
            self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ind = 0 - n
        forward = head
        previous = follow = None
        while forward:
            ind += 1
            if ind >= 0:
                previous = follow
                follow = follow.next if follow else head

            forward = forward.next

        if follow:
            if previous:
                previous.next = follow.next
                del follow
                return head
            else:
                return follow.next


l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)


sol = Solution()
node = sol.removeNthFromEnd(l1, 5)
while node:
    print(node.val, end='')
    node = node.next

print('\n---')
l2 = ListNode(2)
l1 = ListNode(1, l2)
node = sol.removeNthFromEnd(l1, 1)
while node:
    print(node.val)
    node = node.next
