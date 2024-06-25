

class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        self.cut = value
        self.next = next_node
        self.prev = prev_node
        self.index = value[0]


n = int(input())
head = Node(None)
for _ in range(0, n):
    points = list(map(int, input().split(' ')))
    cut = points[0], points[1]

    if head.cut is None:
        head.cut = cut
        continue

    # get_head()
    head_cut = head.cut
    if cut[0] <= head_cut[0] and cut[1] <= head_cut[1]:
        continue

    if cut[0] <= head_cut[0] and cut[1] > head_cut[1]:
        node = head.next
        if node is None:
            head.cut = head_cut[0], points[1]
            continue

        while node:
            if node.cut[0] <= cut[1] <= node.cut[1]:
                node.prev.cut[1] = node.cut[1]
                node.prev.next = node.next
                break
            elif node.cut[1] < cut[1]:
                node = node.next

            elif node.cut[0] > cut[1]:
                node.prev.cut[1] = cut[1]
                break