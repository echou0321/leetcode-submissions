# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.good = 0

        def dfs(node, MAX):
            if not node: return
            if node.val >= MAX:
                MAX = node.val
                self.good += 1
            dfs(node.left, MAX)
            dfs(node.right, MAX)
        dfs(root, root.val)
        return self.good