# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        order = []
        if not list1 and not list2:
            return None

        while list1 or list2:
            if list1:
                order.append(list1)
                list1 = list1.next
            if list2:
                order.append(list2)
                list2 = list2.next

        order.sort(key=lambda x: x.val)
        for i in range(len(order) - 1):
            node = order[i]
            node.next = order[i + 1]

        return order[0]

    def mergeTwoListsIteratively(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next

    def mergeTwoListsRecursively(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoListsRecursively(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursively(list1, list2.next)
            return list2


node4 = ListNode(4)
node2 = ListNode(2, node4)
node1 = ListNode(1, node2)

node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_1 = ListNode(1, node_3)
sol = Solution()

# head = sol.mergeTwoLists(node1, node_1)
# while head:
#     print(head.val)
#     head = head.next

head = sol.mergeTwoListsRecursively(node1, node_1)
while head:
    print(head.val)
    head = head.next
