# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def recur(root):
            if not root:
                return [0, -math.inf]
            
            left = recur(root.left)
            right = recur(root.right)

            currSum = root.val + max(left[0], right[0], 0)
            pathSum = root.val + max(left[0], 0) + max(right[0], 0)
            maxSum = max(currSum, pathSum, left[1], right[1])

            return [currSum, maxSum]

        return recur(root)[1]