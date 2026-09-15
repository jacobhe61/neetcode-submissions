# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        dq = deque([tuple([root, root.val])])
        while dq:
            for n in dq.copy():
                curr = dq.popleft()
                node = curr[0]
                high = curr[1]
                if node:
                    if node.val >= high:
                        high = node.val
                        res += 1
                    dq.append(tuple([node.left, high]))
                    dq.append(tuple([node.right, high]))
        return res