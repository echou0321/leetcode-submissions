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

        def dfs(root, maxSoFar):
            if not root: return 
            if root.val >= maxSoFar:
                maxSoFar = root.val
                self.good += 1
            dfs(root.left, maxSoFar)
            dfs(root.right, maxSoFar)
        
        dfs(root, root.val)
        return self.good
