# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def recur(root):
            nonlocal arr

            if not root:
                return True
            
            cond1 = recur(root.left)
            if arr and root.val <= arr[-1]:
                return False
            arr.append(root.val)
            cond2 = recur(root.right)
            return cond1 and cond2
        
        return recur(root)