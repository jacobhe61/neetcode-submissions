# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr1 = root
        curr2 = root
        while curr1.val != p.val or curr2.val != q.val:
            if curr1.val == curr2.val:
                res = curr1
            if p.val > curr1.val:
                curr1 = curr1.right
            elif p.val < curr1.val:
                curr1 = curr1.left
            else:
                curr1 = curr1
            if q.val > curr2.val:
                curr2 = curr2.right
            elif q.val < curr2.val:
                curr2 = curr2.left
            else:
                curr2 = curr2
        return res
            