# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(a, b):
            if not a and not b:
                return True
            
            if a and not b:
                return False
            
            elif b and not a:
                return False
            
            if a.val != b.val:
                return False
            
            left = helper(a.left, b.left)
            right = helper(a.right, b.right)

            return left and right
        
        return helper(p, q)