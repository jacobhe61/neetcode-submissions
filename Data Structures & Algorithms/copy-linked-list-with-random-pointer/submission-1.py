"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = defaultdict(Node)

        curr = head
        seen[curr] = Node(curr.val, None, None) if curr else None
        result = seen[curr]
        while curr:
            if curr.next not in seen:
                seen[curr.next] = Node(curr.next.val, None, None) if curr.next else None
            seen[curr].next = seen[curr.next]
            if curr.random not in seen:
                seen[curr.random] = Node(curr.random.val, None, None) if curr.random else None
            seen[curr].random = seen[curr.random]
            curr = curr.next
        
        return result
        
