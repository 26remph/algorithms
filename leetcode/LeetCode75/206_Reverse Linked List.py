# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            head.next, tail, head = tail, head, head.next
        return tail

    def reverseListFast(self, head):
        prev = None
        # Run a loop till curr points to NULL...
        while head:
            # Initialize next pointer as the next pointer of curr...
            next = head.next
            # Now assign the prev pointer to curr’s next pointer.
            head.next = prev
            # Assign curr to prev, next to curr...
            prev = head
            head = next
        return prev       # Return the prev pointer to get the reverse linked list...


    def reverseListRecursion(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next:
            lastnode = self.reverseListRecursion(head.next)
            head.next.next = head
            head.next = None
            return lastnode

        return head

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
sol = Solution()

# head = sol.reverseList(node1)
# head = sol.reverseListFast(node1)
head = sol.reverseListRecursion(node1)
while head:
    print(head.val)
    head = head.next
