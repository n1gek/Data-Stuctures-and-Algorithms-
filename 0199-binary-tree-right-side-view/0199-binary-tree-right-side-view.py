# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        stack = deque([root])

        res = []

        while stack:
            length = len(stack)

            for i in range(len(stack)):
                curr = stack.pop()

                if i == length - 1:
                    res.append(curr.val)
                
                if curr.left:
                    stack.appendleft(curr.left)
                if curr.right:
                    stack.appendleft(curr.right)
        
        return res

                




