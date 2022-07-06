# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def get_node_by_index(node, idx):

    while idx and node is not None:
        node = node.next_item
        idx -= 1

    return node


def solution(node, idx):
    # Your code
    # ヽ(´▽`)/
    if idx == 0:
        return node.next_item

    prev = get_node_by_index(node, idx - 1)
    if prev is not None:
        cur_node = prev.next_item
        prev.next_item = None if cur_node is None else cur_node.next_item

    return node

# def print_rezult(node):
#     while node:
#         print(node.value)
#         node = node.next_item


# def test():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     new_head = solution(node0, 1)
#     # result is node0 -> node2 -> node3
#     print_rezult(new_head)

# test()