# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def recur(root):
            nonlocal res

            if not root.left and not root.right:
                return tuple([root.val,root.val])
            
            if not root.left:
                right = recur(root.right)
                high = right[0]

                if root.val >= high:
                    res = False

                return tuple([root.val, right[1]])

            if not root.right:
                left = recur(root.left)
                low = left[1]

                if root.val <= low:
                    res = False

                return tuple([left[0], root.val])


            left = recur(root.left)
            right = recur(root.right)

            low = left[1]
            high = right[0]
            
            if root.val >= high:
                res = False
            if root.val <= low:
                res = False
            return tuple([left[0], right[1]])
        
        recur(root)
        return res
