# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visiting = {id(head): head}
        # print(visiting)
        while head.next:
            _id = id(head.next)
            isVisiting = visiting.get(_id)
            if isVisiting:
                return visiting[_id]

            visiting[_id] = head.next
            head = head.next

    # https://leetcode.com/problems/linked-list-cycle-ii/discuss/1701128/C%2B%2BJavaPython-Slow-and-Fast-oror-Image-Explanation-oror-Beginner-Friendly
    def detectCycleLoop(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head

sol = Solution()
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head = ListNode(3)

node3.next = node1
node2.next = node3
node1.next = node2
head.next = node1

# while head:
#     print(head.val)
#     head = head.next

# head = sol.detectCycle(head)
head = sol.detectCycleLoop(head)
# while head:
#     print(head.val)
#     head = head.next
print(head.val)
assert head == node1
