# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #UMPIRE

        def helper(node, curr):
            if not node:
                return 0
            
            if node.val >= curr:
                isGood = 1 
            else:
                isGood = 0

            
            left = helper(node.left, max(curr, node.val))
            right = helper(node.right, max(curr, node.val))

            return isGood + left + right

        return helper(root, root.val)
            
            



        