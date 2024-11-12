# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        ans = []
        level = []
        level.append([root])
        ans.append([root.val])

        while level:
            visited = level.pop()
            child_node = []
            while visited:
                node = visited.pop()
                if node.left:
                    child_node.append(node.left)
                if node.right:
                    child_node.append(node.right)

            level.clear()
            if child_node:
                level.append(list(reversed(child_node)))
                ans.append(list(x.val for x in child_node))

        return ans

    def levelOrderRecursion(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(node, lvl, ans):
            if node:
                # print(lvl, node.val)
                if len(ans) < lvl + 1:
                    ans.append([])
                ans[lvl].append(node.val)
                dfs(node.left, lvl + 1, ans)
                dfs(node.right, lvl + 1, ans)

        dfs(root, 0, ans)

        return ans


sol = Solution()
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, left=node4)
node3 = TreeNode(3, right=node5)
node1 = TreeNode(1, node2, node3)

# print(sol.levelOrder(node1))
print(sol.levelOrderRecursion(node1))
