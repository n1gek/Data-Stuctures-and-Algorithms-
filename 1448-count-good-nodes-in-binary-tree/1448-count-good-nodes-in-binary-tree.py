# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #UMPIRE
        self.count = 0

        def helper(node, curr):
            if not node:
                return 0
            
            if node.val >= curr:
                self.count += 1
            
            left = helper(node.left, max(curr, node.val))
            right = helper(node.right, max(curr, node.val))


        helper(root, root.val)

        return self.count
            
            



        