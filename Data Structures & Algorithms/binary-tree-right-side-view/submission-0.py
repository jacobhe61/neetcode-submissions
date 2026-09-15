# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque([root])
        res = []
        while dq:
            level = []
            for n in dq.copy():
                curr = dq.popleft()
                if curr:
                    dq.append(curr.left)
                    dq.append(curr.right)
                    level.append(curr.val)
            if level:
                res.append(level[-1])
        return res