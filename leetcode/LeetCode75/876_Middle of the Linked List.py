from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, j = 0, 0
        center = (j, head)
        while head:
            i += 1
            j = i // 2
            if j > center[0]:
                center = (j, center[1].next)
            head = head.next

        return center[1]


node6 = ListNode(6)
node5 = ListNode(5)
# node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
sol = Solution()

head = sol.middleNode(node1)
print(head.val)
