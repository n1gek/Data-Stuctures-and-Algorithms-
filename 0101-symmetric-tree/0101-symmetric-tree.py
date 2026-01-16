# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # make a helper function to change either branch to face a different direction
        # now check for similarity
        if root is None:
            return True

        def helper(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            
            if not nodeA or not nodeB:
                return False
            
            if nodeA.val != nodeB.val:
                return False
            
            return (helper(nodeA.right, nodeB.left) and
            helper(nodeA.left, nodeB.right))

        
        nodeA = root.left
        nodeB = root.right

        return helper(nodeA, nodeB)

