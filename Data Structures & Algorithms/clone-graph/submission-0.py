"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import collections

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        dq = deque()
        visited = set()

        dq.append(node)
        visited.add(node.val)

        res = {}
        while dq:
            curr = dq.popleft()
            
            if curr not in res:
                res[curr] = Node(curr.val)
            
            for n in curr.neighbors:
                if n not in res:
                    res[n] = Node(n.val)

                res[curr].neighbors.append(res[n])

                if n.val in visited:
                    continue

                dq.append(n)
                visited.add(n.val)
        
        return res[node]