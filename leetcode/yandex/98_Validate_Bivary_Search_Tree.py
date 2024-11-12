# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")

        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not (inorder(node.left) and prev < node.val):
                return False
            print(prev, "<", node.val)
            prev = node.val
            return inorder(node.right)

        return inorder(root)

    def var_isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            if lower < node.val < upper:
                return dfs(node.left, lower, node.val) and dfs(
                    node.right, node.val, upper
                )
            else:
                return False

        return dfs(root, lower=float("-inf"), upper=float("inf"))


if __name__ == "__main__":
    # add on
    node16 = TreeNode(16, None, None)
    # ---
    node18 = TreeNode(18, node16, None)
    node4 = TreeNode(4, None, None)
    node12 = TreeNode(12, None, None)
    node24 = TreeNode(24, None, None)
    node31 = TreeNode(31, None, None)
    node44 = TreeNode(44, None, None)
    node66 = TreeNode(66, None, None)
    node90 = TreeNode(90, None, None)
    node10 = TreeNode(10, node4, node12)
    node22 = TreeNode(22, node18, node24)
    node35 = TreeNode(35, node31, node44)
    node70 = TreeNode(70, node66, node90)
    node15 = TreeNode(15, node10, node22)
    node50 = TreeNode(50, node35, node70)
    node25 = TreeNode(25, node15, node50)

    sol = Solution()
    print(sol.isValidBST(node25))
