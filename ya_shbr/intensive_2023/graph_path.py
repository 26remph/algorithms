class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root):
    from collections import deque

    deq = deque()

    deq.append(root.left)
    deq.append(root.right)

    while deq:
        node = deq.popleft()
        if node.left is not None:
            deq.append(node.left)
        if node.right:
            deq.append(node.right)

        print(node.val)


if __name__ == "__main__":
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    node9 = Node(9, node7, node8)
    node3 = Node(3, node4, node5)
    node2 = Node(2, node3, node6)
    root = Node(1, node2, node9)
    solution(root)
