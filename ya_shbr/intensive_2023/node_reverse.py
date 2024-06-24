class Node:

    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def solution():
    ...


if __name__ == '__main__':
    node_d = Node('d')
    node_c = Node('c', node_d)
    node_b = Node('b', node_c)
    node_a = Node('a', node_b)

    solution()
