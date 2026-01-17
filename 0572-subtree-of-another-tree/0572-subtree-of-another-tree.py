# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        def sameTree(a, b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            left = sameTree(a.left, b.left)
            right = sameTree(a.right, b.right)

            return left and right
        
        # not traverse the tree, checking for any node that is equal to the subRoot and pass it to the function
        if root.val == subRoot.val:
            if sameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        