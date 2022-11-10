# Definition for a Node.
from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def preorder(self, root: 'Node') -> List[int]:

        def dfs(node, order):

            if node:
                order.append(node.val)
                for children in node.children:
                    dfs(children, order)

            return order

        return dfs(root, [])

    def preorderNonRecursion(self, root: 'Node') -> List[int]:
        nodes_visited = deque()
        nodes_visited.append(root)
        ans = []
        while nodes_visited:
            cur_node = nodes_visited.popleft()
            for child in reversed(cur_node.children):
                nodes_visited.appendleft(child)
            ans.append(cur_node.val)

        return ans


node5 = Node(5, [])
node6 = Node(6, [])
node2 = Node(2, [])
node4 = Node(4, [])
node3 = Node(3, [node5, node6])
root = Node(1, [node3, node2, node4])

sol = Solution()
print(sol.preorder(root))
print(sol.preorder(root))
# print(sol.preorderNonRecursion(root))
