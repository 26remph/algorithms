class Node:
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val


n = int(input())
m = int(input())

head = None
for i in range(m):
    s, e = map(int, input().split(' '))
    if i == 0:
        head = Node(val=(s, e))
    else:
        head = Node(next=head, val=(s, e))

    prev, cur = head, head.next
    while cur is not None:
        if1 = cur.val[0] <= s <= cur.val[1]
        if2 = cur.val[0] <= e <= cur.val[1]
        if3 = cur.val[0] <= s <= e <= cur.val[1]
        if4 = s <= cur.val[0] <= cur.val[1] <= e
        if any([if1, if2, if3, if4]):
            prev.next = cur.next
            cur = cur.next
        else:
            prev, cur = cur, cur.next

    # line = []
    # prev, cur = head, head.next
    # line.append(head.val)
    # while cur is not None:
    #     line.append(cur.val)
    #     cur = cur.next
    # print(line)

line = []
ans = 0
if head:
    prev, cur = head, head.next
    line.append(head.val)
    ans = 1
    while cur is not None:
        ans += 1
        line.append(cur.val)
        cur = cur.next

print(ans)
