# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def dorianfinneysmith(root):
            if not root: return 0

            left, right = dorianfinneysmith(root.left), dorianfinneysmith(root.right)

            if abs(right - left) > 1:
                self.balance = False
            return max(left, right) + 1
        
        dorianfinneysmith(root)
        return self.balance

            
