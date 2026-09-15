# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameVal(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if not subRoot and root:
            return False
        return root.val == subRoot.val

    def sameTree(self, root, subRoot):
        if not self.sameVal(root, subRoot):
            return False
        if not root and not subRoot:
            return True
        
        leftMatch = self.sameTree(root.left, subRoot.left)
        rightMatch = self.sameTree(root.right, subRoot.right)

        return leftMatch and rightMatch

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.sameVal(root, subRoot) and self.sameTree(root, subRoot):
            return True
        
        leftMatch = self.isSubtree(root.left, subRoot)
        rightMatch = self.isSubtree(root.right, subRoot)

        return leftMatch or rightMatch