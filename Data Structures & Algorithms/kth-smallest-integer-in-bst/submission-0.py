# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        count = 0

        def inOrder(node, k):
            if not node: return
            nonlocal count
            left = inOrder(node.left, k)
            if left is not None:
                return left
            count += 1
            if count == k:
                return node.val
            right = inOrder(node.right, k)
            if right is not None:
                return right
        
        return inOrder(root, k)
        