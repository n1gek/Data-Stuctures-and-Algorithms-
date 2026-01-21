"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node
        
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])

        while q:
            current = q.popleft()

            for n in current.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    q.append(n)
                
                current_clone = visited[current]
                cloned_neighbor = visited[n]
                current_clone.neighbors.append(cloned_neighbor)
        


        return visited[node]