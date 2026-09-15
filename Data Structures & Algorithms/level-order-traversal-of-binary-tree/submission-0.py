# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([root])
        res = []

        while dq:
            subRes = []
            for n in dq.copy():
                curr = dq.popleft()
                if curr:
                    subRes.append(curr.val)
                    dq.append(curr.left)
                    dq.append(curr.right)
            if subRes:
                res.append(subRes)
        return res