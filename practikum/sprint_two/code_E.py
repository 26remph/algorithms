# Comment it before submitting
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def solution(node):
    # Your code
    # ヽ(´▽`)/

    while node:
        node.next, node.prev = node.prev, node.next
        print(node.value)
        if node.next:
            print('next:', node.next.value)
        else:
            print('next:', None)

        if node.prev:
            print('prev:', node.prev.value)
        else:
            print('prev:', None)
        if node.prev:
            node = node.prev
        else:
            break

    return node

def print_rez(node):
    print(node, '>')
    while node:
        print(node.value)
        node = node.next

def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    print_rez(new_head)
    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1

test()