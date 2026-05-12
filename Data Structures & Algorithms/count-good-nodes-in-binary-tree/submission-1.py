# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        good = 0
        maxSoFar = 0

        def dfs(root, maxSoFar):
            if not root: return
            nonlocal good
            if root.val >= maxSoFar:
                good += 1
            maxSoFar = max(maxSoFar, root.val)

            left, right = dfs(root.left, maxSoFar), dfs(root.right, maxSoFar)
        
        dfs(root, root.val)
        return good


